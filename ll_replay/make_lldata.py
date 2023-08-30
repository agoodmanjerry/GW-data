#!/bin/python3

import glob
from gwpy.timeseries import TimeSeriesDict
from lalframe import utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ifo", default=None, help="The Name of the detector.")
parser.add_argument("-S", "--source", default=None, help="The directory of the source gwf files.")
parser.add_argument("-s", "--start", default=None, type=float, help="The start GPS time.")
parser.add_argument("-e", "--end", default=None, type=float, help="The end GPS time.")
parser.add_argument("-d", "--destination", default=None, help="The directory to output the 1-second gwf files.")
parser.add_argument("-t", "--tag", default=None, help="The tag of the output 1-second gwf files.")
args = parser.parse_args()

def make_ll_gwf(ifo, source, channels, start, end, destination, tag):
    data = TimeSeriesDict.read(
        source=source,
        channels=channels,
        start=start,
        end=end,
    )
    
    duration = end - start
    i = 0
    while i < duration:
        ll = data.copy()
        lldata = ll.crop(start + i, start + (i+1), copy=False)
        lldata.write(f'{destination}/{ifo[0]}-{ifo}_{tag}-{int(lldata[channels[0]].t0.value)}-{int(lldata[channels[0]].duration.value)}.gwf', format='gwf')
        i += 1

def main():
    ifo = args.ifo
    source = args.source
    start = args.start
    end = args.end
    destination = args.destination
    tag = args.tag

    f_list = glob.glob(f'{source}/*.gwf')
    ch_list = utils.frtools.get_channels(f_list[0])

    make_ll_gwf(
        ifo,
        f_list,
        ch_list,
        start,
        end,
        destination,
        tag
    )

if __name__ == "__main__":
    main()
