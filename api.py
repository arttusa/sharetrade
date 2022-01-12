import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '..\imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/posts')
def get_posts():
    # Implement method to get first ten posts from db and possibly more
    return "Ok"

# Method for adding a post to database and pic to disc
@app.route('/addpost', methods=['GET', 'POST'])
@cross_origin()
def add_post():
    file = request.files['Chart']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # TODO Implement filename generator
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        # TODO Add other information to the database
        print("File saved" + path)
        return "Ok"

    return "File not correct type"


@app.route('/vote')
def vote():
    # Implement method for upvoting and downvoting
    return "Ok"