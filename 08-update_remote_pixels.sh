#!/bin/bash

cd data

s3shortcut=EMBL
bucket=dinoflagellate-atlas

find . -type f -iname '.zattrs' | while IFS= read -r  file ;do

  echo uploading $file

  f1=${file//\.\/}

  mc cp $file $s3shortcut/$bucket/$f1

  done