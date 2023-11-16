#!/bin/bash

for i in $(cat /home/chia-jui.chou/O3GK_condor/check/problem_list.txt)
do
    scp -i /home/chia-jui.chou/.ssh/id_rsa /home/chia-jui.chou/O3GK_condor/K1_data/K-K1_DATA-$i-4096.gwf chiajui.chou@ldas-grid.ligo.caltech.edu:/home/chiajui.chou/O3GK/K1_strain
done