#!/bin/env bash

set -e


TEMP_FOLDER=$(mktemp -d)

pushd ${TEMP_FOLDER} > /dev/null

for i in $(kubectl get pods -o custom-columns='NAME:metadata.name')
do
   if [[ ${i} = "NAME" ]]
   then
       continue
   fi
   kubectl logs ${i} > ${i}_$(date +"%F-%H-%M-%S").txt
done

#file manager for linux
Thunar . &

#file manager for mac
#open .

popd > /dev/null
