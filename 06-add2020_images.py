import mobie
import os
import glob
import multiprocessing

from functools import partial

datasets = ['VSM20_A1_AM1', 'VSM20_A2_PM1', 'VSM20_A3_AM2', 'VSM20_A4_PM2', 'VSM20_A5_AM3', 'VSM20_A6_PM3']
source_dirs = ['tifA1-vsm20_bc', 'tifA2-vsm20_bc', 'tifA3-vsm20_bc', 'tifA4-vsm20_bc', 'tifA5-vsm20_bc', 'tifA6-vsm20_bc']


dataset, source_dir = list(zip(datasets, source_dirs))[5]


def add_tif(imfile, skip_add_to_dataset, target, max_jobs):
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
                        tmp_folder=None, target=target,
                        max_jobs=max_jobs,
                        view=None, transformation=None,
                        unit="nm",
                        skip_add_to_dataset=skip_add_to_dataset)


def add_images():
    imfiles = glob.glob(source_dir + '/*.tif')

    # Pass one: convert the data, but don't add the source to the dataset to avoid parallel writes to
    # the dataset.json file and corresponding race conditions
    pool = multiprocessing.Pool(25)
    # NOTE: I am not sure if it actually makes sense to use more than one internal job (max_jobs) when using tif inputs.
    # The logic behind this is optimized for chunked data formats and might slow down throughput for tifs rather than speeding it up.
    pool.map(partial(add_tif, skip_add_to_dataset=True, target="slurm", max_jobs=6), imfiles)

    # Pass two: just add the source to the dataset for all images.
    # Note: the computation will not be redone if the tmp_... folders are not removed in betweeen.
    # So only remove the tmp folders afterwards.
    for imfile in imfiles:
        add_tif(imfile, skip_add_to_dataset=False, target="local", max_jobs=1)


if __name__ == '__main__':
    add_images()
