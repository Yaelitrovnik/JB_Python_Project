#!/bin/bash
# Installing nginx on a machine instance based on its name.

vm_name=$1
LOG_FILE="../logs/provisioning.log"  

timestamp() {
    date '+%Y-%m-%d %H:%M:%S'
}

if [[ ! -z $vm_name ]]; then
    echo "$(timestamp) - Starting Nginx installation on '$vm_name'..." | tee -a $LOG_FILE
    sleep 2  # Simulate installation
    echo "$(timestamp) - Installation successful on '$vm_name'." | tee -a $LOG_FILE
else
    echo "$(timestamp) - Error: Please pass vm_name as an argument." | tee -a $LOG_FILE
    exit 1
fi
