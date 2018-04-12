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
        # TODO: Map all processing config vars here
        pass

    # All the juicy stuff happens here!
    def process(self, config):
        
        playlistIds = []

        playlistObject = pafy.get_playlist2(config['playlistUrl'])
        print('Playlist has ' + str(len(playlistObject)) + ' vids.')
        bar = Bar('Retrieving playlist info', max=len(playlistObject), suffix='%(index)d/%(max)d - %(percent).1f%%')
        for vidObj in playlistObject:
                playlistIds.append(vidObj.videoid)
                bar.next()
        bar.finish()

        vidsToDl = []
        if config['pickRandom']:
            vidsToDl = random.sample(playlistIds, 2)
        else:
            # TODO: take n first videos from playlistIds
            pass

        tempVidPath = './temp_vids'
        if not os.path.exists(tempVidPath):
            os.makedirs(tempVidPath)
            
        for vid in vidsToDl:
            v = pafy.new(vid)
            s = v.getbest(preftype="mp4") # in the future make this a parameter to choose resolution
            filename = s.download(filepath="./temp_vids/" + vid + ".mp4")

        vids = []
        # TODO: for v2, let users upload a intro video
        # vids.append(VideoFileClip("intro.mp4"))
        for vid in vidsToDl:
            vids.append(VideoFileClip("./temp_vids/" + vid + ".mp4"))
        
        final = concatenate_videoclips(vids, method='compose')

        # TODO: read FPS from config
        final.write_videofile("final.mp4", fps=30) 

        return "Return something here"
        #shutil.rmtree('./temp_vids/')
