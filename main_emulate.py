from main import hello_world, hello_world_test 

if __name__ == "main_emulate":
    """ Runs python 3.7 Cloud Functions locally
    Conditions:
        * __main__ : being run directly
        * main : being run on debugger

        Flask app wrapper
    """
    from flask import Flask, request, send_from_directory
    from flask_cors import CORS, cross_origin
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/dissident-images-clf', methods=['GET', 'POST'])
    @cross_origin()
    def dissident_images_clf():
        return hello_world_test(request)

    @app.route('/images/<path:path>')
    @cross_origin()
    def send_image(path):
        return send_from_directory('../../images', path)

    app.run('localhost', 5000, debug=True)