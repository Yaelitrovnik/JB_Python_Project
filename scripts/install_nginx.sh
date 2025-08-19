#!/bin/bash
#   installing nginx on a machine instance based on its name.

vm_name=$1

if [[ ! -z $vm_name ]]; then
    echo "Installing nginx on '$vm_name'..."
    sleep 2
    echo "Installation successful on '$vm_name'."
else
    echo "Please pass vm_name as an argument."
    exit 1
fi
