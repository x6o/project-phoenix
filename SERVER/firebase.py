# import firebase_admin
# from firebase_admin import credentials, db, storage

# cred = credentials.Certificate('spliceer-video-firebase-adminsdk-81pru-4143e2521a.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL' : 'https://spliceer-video.firebaseio.com/'
# })

# storageBucket = storage.bucket('spliceer-video.appspot.com')
# print storageBucket

# # storageBucket.upload_from_filename(filename='fi.txt')
# # result = storageBucket.get_blob('user-videos/fi.mp4')
# # print result.public_url

# # client = _get_storage_client()
# blob = storageBucket.blob('user-videos/fi.mp4')

# blob.upload_from_filename("fi.mp4")

# url = blob.public_url
# print url

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('spliceer-video-firebase-adminsdk-81pru-4143e2521a.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://spliceer-video.firebaseio.com/'
})
ref = db.reference()
requests_ref = ref.child('requests')

new_entry = {
    "requestId": 1,
    "playlistUrl": "https://www.youtube.com/playlist?list=PLhCGrfbSCqDkuv9Gh5mZ85gwZqczL12bT",
    "numberVideos": 2,
    "videosFps": 30,
    "pickRandom": True
}

requests_ref.push(new_entry)