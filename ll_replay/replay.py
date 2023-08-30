#!/bin/python

import os
import time

replay_start = 1369291863
duration = 16384
keep = 300
frame_length = 1

ifo = "K1"
hoft_src = f"/data/ll_data/llhoft_buffer/{ifo}"
woft_src = f"/data/ll_data/lldetchar_buffer/{ifo}"
hoft_dest = f"/data/ll_data/kafka/{ifo}"
woft_dest = f"/data/ll_data/lldetchar/{ifo}"

# increments by one after writing every frame-set (L1 H1 both hoft and woft)
total_streaming_time_should_now_be = 0

begin = time.time()
for start in range(replay_start, replay_start+duration):
    try:
        # strain channel frames
        hoft_from = f"{hoft_src}/{ifo[0]}-{ifo}_llhoft-{start}-1.gwf"
        hoft_to = f"{hoft_dest}/{ifo[0]}-{ifo}_llhoft-{start}-1.gwf"

        # witness channel frames
        woft_from = f"{woft_src}/{ifo[0]}-{ifo}_lldetchar-{start}-1.gwf"
        woft_to = f"{woft_dest}/{ifo[0]}-{ifo}_lldetchar-{start}-1.gwf"

        # copy the frames to destination
        os.system(f"cp {hoft_from} {hoft_to}")
        os.system(f"cp {woft_from} {woft_to}")
        
        # Delete previous files if the number of the files in the destination is larger than the keep nunber.
        count = start - replay_start
        if count >= keep:
            os.system(f"rm {hoft_dest}/{ifo[0]}-{ifo}_llhoft-{start-keep}-1.gwf")
            os.system(f"rm {woft_dest}/{ifo[0]}-{ifo}_lldetchar-{start-keep}-1.gwf")

    except KeyboardInterrupt:
        print ("KeyboardInterrupt")

    #except:
        #pass

    # print (start, " written")
    total_streaming_time_should_now_be += 1
    total_time_elapsed_so_far = time.time() - begin
    wait  = total_streaming_time_should_now_be - total_time_elapsed_so_far
    time.sleep(wait)

