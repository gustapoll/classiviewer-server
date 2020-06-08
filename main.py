import json
import requests
from image_classifier import predict
from flask import jsonify

def hello_world(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (jsonify(hello_world_test(request)), 200, headers)

def hello_world_test(request):

    if 'dissidentImg' in request.files:
        photos = request.files.getlist('dissidentImg')
        for photo in photos:
            if photo.filename != '':            
                photo.save('./images/' + photo.filename)

        res = predict([x.filename for x in photos])

    # Loaded Image that user selected to classify (frontend: Overview tab)
    elif len(request.data) > 0: # if has data
        photos = json.loads(request.data)
        for photo in photos:
            if photo['name'] != '':
                photo.save('./images/' + photo['name'])
        
        res = predict([x.filename for x in photos])
    else:
        raise Exception('CUSTOM ERROR: Unimplemented State.')

    return jsonify(res)
