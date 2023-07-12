import mobie
import os
import glob
import multiprocessing

datasets = ['VSM21_A1_AM1', 'VSM21_A2_PM1', 'VSM21_A3_AM2', 'VSM21_A4_PM2', 'VSM21_A5_PM3', 'VSM21_A6_AM3']
source_dirs = ['tifA1-vsm21_bc', 'tifA2-vsm21_bc', 'tifA3-vsm21_bc', 'tifA4-vsm21_bc', 'tifA5-vsm21_bc', 'tifA6-vsm21_bc']


dataset, source_dir = list(zip(datasets, source_dirs))[5]

def add_tif(imfile):
    ds = mobie.metadata.read_dataset_metadata('./data/' + dataset)

    imname = dataset + '_' + os.path.basename(imfile).split(os.extsep)[0].split('-')[2]

    if imname not in ds['sources'].keys():
        print('adding ' + imname + 'to mobie project.')
        mobie.add_image(imfile, '',
                        './data', dataset,
                        imname,
                        [0.597] * 2, [[2, 2]] * 6, [512, 512],
                        file_format="ome.zarr", menu_name="EM",
                        tmp_folder=None, target="slurm",
                        max_jobs=2,
                        view=None, transformation=None,
                        unit="nm", )

def add_images():
    pool = multiprocessing.Pool(5)

    imfiles = glob.glob(source_dir + '/*.tif')

    pool.map(add_tif, imfiles)


if __name__ == '__main__':
    add_images()