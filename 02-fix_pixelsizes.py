import os
import mobie
import json


root = 'data'

depth = 7
scale = 2
pxs = 1.676

for dataset in mobie.metadata.get_datasets(root):
    dataset_folder = os.path.join(root,dataset)
    zarr_folder = os.path.join(dataset_folder,'images','ome-zarr')
    for im in os.listdir(zarr_folder):

        print('updating pixel sizes for ' + im)

        with open(os.path.join(zarr_folder, im, '.zattrs')) as f:
            zattrs = json.load(f)

        for d in range(depth):
            thispixel = pxs * (scale ** d)
            zattrs['multiscales'][0]['datasets'][d]['coordinateTransformations'][0]['scale'] = [thispixel] * 2

        with open(os.path.join(zarr_folder, im, '.zattrs'), 'w') as f:
            json.dump(zattrs,f)