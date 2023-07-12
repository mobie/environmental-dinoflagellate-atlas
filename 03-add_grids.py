import mobie
import os

root = 'data'

for dataset in mobie.metadata.get_datasets(root):
    dataset_folder = os.path.join(root,dataset)

    view_name = dataset

    ds = mobie.metadata.read_dataset_metadata(dataset_folder)

    sources = list()

    for source in ds['sources'].keys():
        if view_name in source:
            sources.append([source])

    mobie.create_grid_view(dataset_folder, view_name, sources, menu_name='sampling_grid')