import mobie
import os

root = 'data'

for dataset in ['cumulative_AM', 'cumulative_PM']:
    dataset_folder = os.path.join(root,dataset)

    ds = mobie.metadata.read_dataset_metadata(dataset_folder)

    sources = [[source] for source in ds['sources'].keys()]

    mobie.create_grid_view(dataset_folder, 'complete_grid', sources, menu_name='grid')