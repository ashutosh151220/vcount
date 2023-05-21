from moviepy.editor import *
from multiprocessing import Process, Semaphore
import sys
video_path=r"E:\Ashu_Practice_1month\test.mp4"
segment_length = 60
frames = 25
print("file loading started........")
pool_sema = Semaphore(6)
original_video = VideoFileClip(video_path)
print("file loading finish........")
duration = original_video.duration
clip_start = 0

num = 0
path=r"E:\Ashu_Practice_1month\agg_folder/"

def write_videofile(clip_start, clip_end):
    try:
        clip = VideoFileClip(video_path).subclip(clip_start, clip_end).resize((704, 576))
        print(clip_start, clip_end)
        clip.write_videofile(path+"output_%s.mp4" % num, fps=frames, bitrate="4000k",
                             threads=4, preset='ultrafast', codec='h264',logger=None)
    except:
        print("error", clip_start, clip_end)
    finally:
        pool_sema.release()
    


while clip_start < duration:
    clip_end = clip_start + segment_length
    if clip_end > duration:
            clip_end = duration
    pool_sema.acquire()
    write_videofile(clip_start, clip_end)
    clip_start = clip_end
    num += 1