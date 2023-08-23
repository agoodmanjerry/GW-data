#!/bin/bash

IFO=K1
TAG=llhoft
START=1369291863
END=1369291864

python make_lldata.py \
    --ifo ${IFO} \
    --source /mnt/f/kagra-o4a-data/${IFO}_${TAG} \
    --start ${START} \
    --end ${END} \
    --destination /mnt/f/kagra-o4a-data/${TAG}_buffer/${IFO} \
    --tag ${TAG}
