import mobie
import os
import glob
import multiprocessing

datasets = ['VSM20_A1_AM1', 'VSM20_A2_PM1', 'VSM20_A3_AM2', 'VSM20_A4_PM2', 'VSM20_A5_PM3', 'VSM20_A6_AM3']
source_dirs = ['tifA1-vsm20_bc', 'tifA2-vsm20_bc', 'tifA3-vsm20_bc', 'tifA4-vsm20bc', 'tifA5-vsm20_bc', 'tifA6-vsm20_bc']


dataset, source_dir = list(zip(datasets, source_dirs))[5]

def add_tif(imfile):
    ds = mobie.metadata.read_dataset_metadata('./data/' + dataset)

    imname = dataset + '_' + os.path.basename(imfile).split(os.extsep)[0].split('-')[2]

    if ds == {}:
        ds['sources'] = {}

    if imname not in ds['sources'].keys():
        print('adding ' + imname + 'to mobie project.')
        mobie.add_image(imfile, '',
                        './data', dataset,
                        imname,
                        [1.676] * 2, [[2, 2]] * 6, [512, 512],
                        file_format="ome.zarr", menu_name="EM",
                        tmp_folder=None, target="slurm",
                        max_jobs=5,
                        view=None, transformation=None,
                        unit="nm", )

def add_images():
    pool = multiprocessing.Pool(10)

    imfiles = glob.glob(source_dir + '/*.tif')

    pool.map(add_tif, imfiles)


if __name__ == '__main__':
    add_images()