# imports
import os
import pafy
import time
import random
import shutil
import firebase_admin
from moviepy.editor import *
from progress.bar import Bar
from firebase_admin import credentials, db, storage

cred = credentials.Certificate('spliceer-video-firebase-adminsdk-81pru-4143e2521a.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://spliceer-video.firebaseio.com/'
})

storageBucket = storage.bucket('spliceer-video.appspot.com')

class VideoProcessing:

    def __init__(self):
        # TODO: Map all processing config vars here
        pass

    # All the juicy stuff happens here!
    def process(self, request):
        ref = db.reference()
        requests_ref = ref.child('requests/{0}'.format(request['requestId']))
        config = requests_ref.get()
        
        if config:
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
            # TODO: for v2, let users upload a video
            # vids.append(VideoFileClip("intro.mp4"))
            for vid in vidsToDl:
                vids.append(VideoFileClip("./temp_vids/" + vid + ".mp4"))
            
            final = concatenate_videoclips(vids, method='compose')

            final.write_videofile("{0}.mp4".format(request['requestId'].replace('-', '_')), fps=config['videosFps'])

            print "Uploading file"
            blob = storageBucket.blob('user-videos/{0}.mp4'.format(request['requestId']))
            blob.upload_from_filename("{0}.mp4".format(request['requestId'].replace('-', '_')))
            return blob.public_url
            

        return None
        #shutil.rmtree('./temp_vids/')
