from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '主页'

@app.route('/messageboard')
def hello():
    return '留言板'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.debug = True
    app.run()