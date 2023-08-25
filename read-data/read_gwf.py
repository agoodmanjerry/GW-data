#!/bin/python

import os
from pathlib import Path
from gwpy.timeseries import TimeSeries
from math import floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ifo", default=None, help="The name of the detector.")
parser.add_argument("-t", "--time", default=None, type=float, help="The time label of the 4-second windows.")
parser.add_argument("-d", "--destination", default=None, help="The destination directory to save the timeseries.")
args = parser.parse_args()

def main():
    ifo = args.ifo
    time = args.time
    destination = args.destination
    os.system(f"mkdir {destination}")

    folder = f"/archive/frames/O3/hoft_C01/{ifo}/{ifo[0]}-{ifo}_HOFT_C01-{floor(time/1e5)}"
    p_folder = f"/archive/frames/O3/hoft_C01/{ifo}/{ifo[0]}-{ifo}_HOFT_C01-{floor(time/1e5)-1}"

    f_list = list(Path(folder).glob("*.gwf"))
    f_list.sort()
    f_start = str(f_list[0])
    f_start = int(f_start.split('-')[-2])
    f_end = str(f_list[-1])
    f_end = int(f_end.split('-')[-2])

    p_list = list(Path(p_folder).glob("*.gwf"))
    p_list.sort()
    p_end = str(p_list[-1])

    f_time = int(f_start + 4096*floor((time - f_start)/4096))

    if (f_time - f_start) < 4:
        source = [p_end, str(f_list[0])]
    elif abs((f_time - (f_start+4096)) <= 2):
        source = [str(f_list[0]), str(f_list[1])]
    else:
        source = [f"{folder}/{ifo[0]}-{ifo}_HOFT_C01-{t}-4096.gwf" for t in range(f_time-4096, f_time + 2*4096, 4096)]
    
    ts = TimeSeries.read(
        source,
        channel=f'{ifo}:DCS-CALIB_STRAIN_CLEAN_C01',
        start=time-2,
        end=time+2
    )
    
    tt = f'{ts.t0.value+2:.6f}'.split('.')
    path = f"{destination}/{ifo}_{tt[0]}-{tt[1]}.hdf5"
    print(path)
    ts.write(path, format='hdf5')

if __name__ == "__main__":
    main()