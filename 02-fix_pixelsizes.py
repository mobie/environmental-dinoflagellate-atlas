import os
import mobie
import json
import numpy as np

root = 'data'

depth = 7
scale = 2

correction = np.loadtxt('pxs_correct.csv', delimiter=",", dtype=str)
correct_pxs = correction[:,1].astype(float)

for dataset in mobie.metadata.get_datasets(root):
    dataset_folder = os.path.join(root,dataset)

    if not 'VSM' in dataset_folder:
        continue

    zarr_folder = os.path.join(dataset_folder,'images','ome-zarr')

    for im in os.listdir(zarr_folder):

        print('updating pixel sizes for ' + im)

        pxs = float(correction[correction[:,0]==im.strip('.ome.zarr'),1])


        with open(os.path.join(zarr_folder, im, '.zattrs')) as f:
            zattrs = json.load(f)

        if len(zattrs['multiscales']) > 1:
            for ms, __ in enumerate(zattrs['multiscales'][1:]):
                zattrs['multiscales'].pop(1)

        for d in range(depth):
            thispixel = pxs * (scale ** d)
            zattrs['multiscales'][0]['datasets'][d]['coordinateTransformations'][0]['scale'] = [thispixel] * 2

        with open(os.path.join(zarr_folder, im, '.zattrs'), 'w') as f:
            json.dump(zattrs,f)