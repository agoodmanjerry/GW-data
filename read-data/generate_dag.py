#!/bin/python

import os
import sys
import h5py as h5
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", default=None, help="The name of dag file.")
parser.add_argument("-i", "--ifo", default=None, help="The name of the detector.")
parser.add_argument("-d", "--destination", default=None, help="The destination directory to save the timeseries.")
parser.add_argument("-t", "--time_stamp", default=None, help="The hdf5 file which include all the triggered time.")
args = parser.parse_args()

name = args.name
if os.path.exists(name):
    print(f"Warning: The dag file {name} has exists. Please use another name.")
    sys.exit()

ifo = args.ifo
destination = args.destination
stamp = args.time_stamp
with h5.File(stamp, 'r') as f:
    time = f[f'{ifo}/time'][:]


with open(name, 'x') as f:
    for i in range(len(time)):
        dagtext = '''JOB {} read_gwf.sub
RETRY {} 0
VARS {} ifo="{}" time="{}" destination="{}"\n
'''.format(f'{ifo}_{i}', f'{ifo}_{i}', f'{ifo}_{i}', ifo, time[i], destination)
        f.writelines(dagtext)
