#!flask/bin/python
from flask import Flask, request, abort, jsonify
from processvideoscript import VideoProcessing
import json

app = Flask(__name__)
class VideoProcessingServer:
    
    # TODO: implement?
    # def __init__(self):
    #     self.processingConfig = None

    @app.route('/')
    def index():
        # no direct calling!
        abort(400)

    @app.route('/process', methods=['POST'])
    def process():
        if not request.json:
            abort(400)

        # Add auth token verification here 

        if 'requestId' in request.json: # TODO: should verify something else..?
            processingConfig = request.json

            # Should verify if id exists
            
            script = VideoProcessing()
            result = script.process(processingConfig)

            returnData = {
                'url': result
            }
        
            return jsonify({'payload': returnData}), 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)