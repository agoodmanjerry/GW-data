#!/bin/bash

IFO=K1
TAG=lldetchar
START=1369291863
END=1369300055

python make_lldata.py \
    --ifo ${IFO} \
    --source /data/ll_data/${IFO}_${TAG} \
    --start ${START} \
    --end ${END} \
    --destination /data/ll_data/${TAG}_buffer/${IFO} \
    --tag ${TAG}
