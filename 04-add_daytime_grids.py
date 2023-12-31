import mobie
import os

root = 'data'
filter = 'M21'

for dataset in ['all_years']:
    dataset_folder = os.path.join(root,dataset)

    ds = mobie.metadata.read_dataset_metadata(dataset_folder)

    sources = [[source] for source in ds['sources'].keys() if filter in source ]

    print('Creating grid view for sources ' + str(sources) +'.')
    if len(sources) > 1: 
        mobie.create_grid_view(dataset_folder, ''.join([dataset,filter]), sources, menu_name='grid')