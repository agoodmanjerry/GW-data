#!/bin/bash

IFO=L1
CHANNELS=/home/chiajui.chou/GW-data/ll_replay/get_data/chanslist.txt
START=1369295959
END=1369369247
LENGTH=4096
DESTINATION=/home/chiajui.chou/ll_data
OUTPUT=/home/chiajui.chou/GW-data/ll_replay/get_data/${IFO}_condor_subs

python get_data_subs.py\
    --ifo ${IFO}\
    --channels ${CHANNELS}\
    --start ${START}\
    --end ${END}\
    --length ${LENGTH}\
    --destination ${DESTINATION}\
    --output ${OUTPUT}