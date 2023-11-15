import mobie
import os

root = 'data'

datasets = ['VSM20_A1_AM1', 'VSM20_A2_PM1', 'VSM20_A3_AM2', 'VSM20_A4_PM2', 'VSM20_A5_AM3', 'VSM20_A6_PM3']

for dataset in datasets:
    dataset_folder = os.path.join(root,dataset)

    view_name = dataset

    ds = mobie.metadata.read_dataset_metadata(dataset_folder)

    sources = list()

    for source in ds['sources'].keys():
        if view_name in source:
            sources.append([source])

    mobie.create_grid_view(dataset_folder, view_name, sources, menu_name='sampling_grid')