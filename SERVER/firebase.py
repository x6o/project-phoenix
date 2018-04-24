import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('spliceer-video-firebase-adminsdk-81pru-c08fc33ea5.json')
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