import os

from flask import Flask, request, render_template, url_for, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/hello', methods=['GET'])
def hello_flask():
    return "Hello! Flask!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_sub_path(sub_path):
    # show the subpath after /path/
    return 'Subpath %s' % sub_path


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/signin', methods=['GET'])
def sign_in_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('sign_in_ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/read-me', methods=['GET'])
def read_me():
    query_parameters = request.args.get('key', '')
    if query_parameters:
        print(query_parameters)
    return render_template(url_for('static', filename='README.html'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST' and 'file' in request.files:
        f = request.files['file']
        f.save(os.getcwd() + '/resources/' + secure_filename(f.filename))
        return 'SUCCESS'
    else:
        return 'FAILURE'


@app.route('/error', methods=['GET'])
def error():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('static/404/index.html'), 404


if __name__ == '__main__':
    app.run()
