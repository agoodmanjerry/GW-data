#!/bin/bash

DATA_DIR=/home/chiajui.chou/ll_data
IFO=K1
TAG=llhoft
START=1369291863
END=1369308247

python make_lldata.py \
    --ifo ${IFO} \
    --source ${DATA_DIR}/${IFO}_${TAG} \
    --start ${START} \
    --end ${END} \
    --destination ${DATA_DIR}/${TAG}_buffer/${IFO} \
    --tag ${TAG}
