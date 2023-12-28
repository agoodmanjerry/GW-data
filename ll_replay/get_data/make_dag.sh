#!/bin/bash

IFO=H1

python get_data_dag.py\
    --ifo ${IFO}\
    --channels /home/chiajui.chou/GW-data/ll_replay/get_data/chanslist.txt\
    --start 1369291863\
    --end 1369369247\
    --length 4096\
    --destination /home/chiajui.chou/ll_data\
    --output /home/chiajui.chou/GW-data/ll_replay/get_data/${IFO}_condor
