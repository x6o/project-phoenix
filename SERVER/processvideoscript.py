# imports
import os
import pafy
import time
import random
import shutil
from moviepy.editor import *
from progress.bar import Bar

class VideoProcessing:

    def __init__(self):
        pass

    # All the juicy stuff happens here!
    # TODO Accept configuration arguments
    def process(self):
        
        # Config

        #memePlaylistUrl = "https://www.youtube.com/playlist?list=PLv3TTBr1W_9tppikBxAE_G6qjWdBljBHJ"
        playlistUrl = "https://www.youtube.com/playlist?list=PLhCGrfbSCqDkuv9Gh5mZ85gwZqczL12bT"

        playlistIds = []

        playlistObject = pafy.get_playlist2(playlistUrl)
        print('Playlist has ' + str(len(playlistObject)) + ' vids.')
        bar = Bar('Retrieving playlist info', max=len(playlistObject), suffix='%(index)d/%(max)d - %(percent).1f%%')
        for vidObj in playlistObject:
                playlistIds.append(vidObj.videoid)
                bar.next()
        bar.finish()

        randomVidsToDl = random.sample(playlistIds, 2)

        tempVidPath = './temp_vids' 
        if not os.path.exists(tempVidPath):
            os.makedirs(tempVidPath)
            
        for vid in randomVidsToDl:
            v = pafy.new(vid)
            s = v.getbest(preftype="mp4")
            filename = s.download(filepath="./temp_vids/" + vid + ".mp4")

        vids = []
        #vids.append(VideoFileClip("intro.mp4"))
        for vid in randomVidsToDl:
            vids.append(VideoFileClip("./temp_vids/" + vid + ".mp4"))
        
        final = concatenate_videoclips(vids, method='compose')
        final.write_videofile("final.mp4", fps=30)
        #shutil.rmtree('./temp_vids/')
