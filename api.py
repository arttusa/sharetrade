from flask import Flask

app = Flask(__name__)


@app.route('/posts')
def get_posts():
    # Implement method to get first ten posts from db and possibly more 
    
    return "Ok"

@app.route('/addpost')
def add_post():
    # Implement method for adding a post to disk
    return "Ok"

@app.route('/vote')
def vote():
    # Implement method for upvoting and downvoting
    return "Ok"