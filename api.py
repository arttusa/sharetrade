import os
import json
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from db_handler import add_post, get_posts

UPLOAD_FOLDER = '.\imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'


def fetch_charts(post_list):
    for post in post_list:
       path = post.path

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Method for adding a post to database and pic to disc
@app.route('/uploadpost', methods=['GET', 'POST'])
@cross_origin()
def upload_post():
    file = request.files['Chart']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # TODO Implement filename generator
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        user = "Mikko"
        symbol = "TSLA"
        description = "Getting ready for a breakout"
        add_post(user, symbol, description, path)
        print("File saved" + path)
        return "Ok"

    return "File not correct type"

# http://localhost:5000/show_image/imgs_2022_01_18/Livermore_Quotes.jpg
@app.route('/show_image/<path:path>', methods=['GET'])
@cross_origin()
def show_image(path):
    # print(path) = imgs_2022_01_18/Livermore_Quotes.jpg
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)

@app.route('/get_posts', methods=['GET'])
@cross_origin()
def posts():
    posts = get_posts()
    return json.dumps(posts)


@app.route('/vote')
def vote():
    # Implement method for upvoting and downvoting
    return "Ok"