
import os
import time
import glob

replay_start = 1251331218

duration = int(24*3600)

frame_length = 1


H1_src = "/home/muhammed.saleem/deepClean/deepclean/deepClean_MDC/pseudo_replay/H1/*-3600/"
L1_src = "/home/muhammed.saleem/deepClean/deepclean/deepClean_MDC/pseudo_replay/L1/*-3600/"

H1_dest = "/home/deep.clean/O4-tests/MDC/pseudo-replay/H1/"
L1_dest = "/home/deep.clean/O4-tests/MDC/pseudo-replay/L1/"



# increments by one after writing every frame-set (L1 H1 both hoft and woft)
total_streaming_time_should_now_be = 0

begin = time.time()
for start in range(replay_start, replay_start+duration):


    # Creating destination directories if they do not already exist

    subdir = str(start//10000)
    H1_hoft_dest_sub = os.path.join(H1_dest, subdir, "llhoft")
    L1_hoft_dest_sub = os.path.join(L1_dest, subdir, "llhoft")
    H1_woft_dest_sub = os.path.join(H1_dest, subdir, "lldetchar")
    L1_woft_dest_sub = os.path.join(L1_dest, subdir, "lldetchar")


    os.makedirs(H1_hoft_dest_sub,  exist_ok = True)
    os.makedirs(L1_hoft_dest_sub,  exist_ok = True)
    os.makedirs(H1_woft_dest_sub,  exist_ok = True)
    os.makedirs(L1_woft_dest_sub,  exist_ok = True)

    try:

        # strain channel frames

        H1_hoft_from = glob.glob(os.path.join(H1_src, "llhoft", f"H-H1_HOFT-{str(start)}-1.gwf"))[0]
        L1_hoft_from = glob.glob(os.path.join(L1_src, "llhoft", f"H-H1_HOFT-{str(start)}-1.gwf"))[0]

        H1_hoft_to = os.path.join(H1_hoft_dest_sub, f"H-H1_HOFT-{str(start)}-1.gwf")
        L1_hoft_to = os.path.join(L1_hoft_dest_sub, f"L-L1_HOFT-{str(start)}-1.gwf")

        # witness channel frames

        H1_woft_from = glob.glob(os.path.join(H1_src, "lldetchar", f"H-H1_Detchar-{str(start)}-1.gwf"))[0]
        L1_woft_from = glob.glob(os.path.join(L1_src, "lldetchar", f"H-H1_Detchar-{str(start)}-1.gwf"))[0]

        H1_woft_to = os.path.join(H1_woft_dest_sub, f"H-H1_Detchar-{str(start)}-1.gwf")
        L1_woft_to = os.path.join(L1_woft_dest_sub, f"L-L1_Detchar-{str(start)}-1.gwf")


        os.system(f"cp {H1_hoft_from} {H1_hoft_to}")
        os.system(f"cp {L1_hoft_from} {L1_hoft_to}")

        os.system(f"cp {H1_woft_from} {H1_woft_to}")
        os.system(f"cp {L1_woft_from} {L1_woft_to}")

    except KeyboardInterrupt:
        print ("KeyboardInterrupt")

    except:
        pass

    print (start, " written")
    total_streaming_time_should_now_be += 1
    total_time_elapsed_so_far = time.time() - begin
    wait  = total_streaming_time_should_now_be - total_time_elapsed_so_far
    time.sleep(wait)


