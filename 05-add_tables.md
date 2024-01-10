## adding tables for MoBIE

- remove columns "imagePath", "a" ... "z"
- add first column "region_id"
- change dashes to spaces to match sources 
- save as `$dataset/tables/default.tsv`
- copy first two columns to scratch file
- format them to fit `regionDisplay`
```JSON
"sources": {
              "0": ["VSM21_A1_AM1_001"],
              "1": ["VSM21_A1_AM1_002"],
              ...
```

`\s+V` -> `": ["V`

`\n` -> `"],\n"`

- add table source to dataset
- add table `regionDisplay` to dataset