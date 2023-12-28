#!/bin/python

from gwpy.timeseries import TimeSeries
from gwpy.timeseries import TimeSeriesDict
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ifo", default=None, help="The name of the detector.")
parser.add_argument("-c", "--channels", default=None, help="The text file that records the channels to be fetched.")
parser.add_argument("-s", "--start", default=None, type=float, help="The start GPS time.")
parser.add_argument("-e", "--end", default=None, type=float, help="The end GPS time.")
parser.add_argument("-d", "--destination", default=None, help="The directory to output the gwf files of the fetched data.")
args = parser.parse_args()

def main():
    ifo = args.ifo
    channels = args.channels
    start = args.start
    end = args.end
    destination = args.destination

    with open(channels, 'r') as f:
        ch_config = f.read()

    ifo_find = re.compile(ifo+':'+r'.*')
    ifo_chlist = ifo_find.findall(ch_config)
    print(ifo_chlist)

    llhoft = TimeSeries.get(
        ifo_chlist[0],
        start=start,
        end=end,
        nproc=8,
        allow_tape=True
    )

    lldetchar = TimeSeriesDict.get(
        channels=ifo_chlist[1:],
        start=start,
        end=end,
        nproc=8,
        allow_tape=True
    )

    llhoft.write(f'{destination}/{ifo}_llhoft/{ifo[0]}-{ifo}_llhoft-{int(start)}-{int(end-start)}.gwf')
    lldetchar.write(f'{destination}/{ifo}_lldetchar/{ifo[0]}-{ifo}_lldetchar-{int(start)}-{int(end-start)}.gwf')

if __name__ == "__main__":
    main()
