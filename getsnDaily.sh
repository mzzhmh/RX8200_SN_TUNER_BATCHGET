#!/bin/bash

tDate=`date +"%Y-%m-%d"`
mv /opt/serialNumber/SAT_RX8200_VAST_SN.csv /opt/serialNumber/SAT_RX8200_VAST_SN.${tDate}.csv

#do the get Serial Number work
nohup /opt/RX8200SNGET/getsn.py &>/opt/RX8200SNGET/logs

