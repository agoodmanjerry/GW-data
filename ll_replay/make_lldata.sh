#!/bin/bash

IFO=K1
TAG=llhoft
START=1369300055
END=1369308247

python make_lldata.py \
    --ifo ${IFO} \
    --source /data/ll_data/${IFO}_${TAG} \
    --start ${START} \
    --end ${END} \
    --destination /data/ll_data/${TAG}_buffer/${IFO} \
    --tag ${TAG}
