#!flask/bin/python
from flask import Flask
from processvideoscript import VideoProcessing

app = Flask(__name__)

@app.route('/')
def index():

    script = VideoProcessing()
    script.process()

    return "Script executed"

if __name__ == '__main__':
    app.run(debug=True)