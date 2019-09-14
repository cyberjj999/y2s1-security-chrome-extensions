from flask import Flask, url_for , request
from flask_cors import CORS

app = Flask(__name__)
#This program is created through flask documentation - http://flask.pocoo.org/docs/1.0/quickstart/
#First do $env:FLASK_APP = "hello.py"
#Then do python -m flask run
CORS(app)

@app.route('/')
def process_URL():
     data = request.get_json()
     print(data)
     return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'
#If you type http://127.0.0.1:5000/hello in the browser
#You will receive the text Hello, World

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
#If you type http://127.0.0.1:5000/user/bob in the browser
#You will receive the text User bob

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
    
#The path quite interesting , if u type /path/abcdef lol 123
#url will appear as http:.../path/abcdef%lol%123
#basically % will appear (cus its apparently a path thing?)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#Diff btwn these 2 is one got trailing / another dont have
#Both will work if u just type /about or /projects
#however , if u type /about/ , then have error 404 not found
#This apparently helps with unique-ness


# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

#Using url_for could be better than just hardcoding
#Look at URL building section

def do_the_login():
     return "Logging in"
     
def show_the_login_form():
     return "Log in here"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

#url_for('static', filename='style.css')

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run()  # Launch built-in web server and run this Flask webapp