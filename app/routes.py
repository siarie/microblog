from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'siarie'}
    posts = [
        {
            'author': {'username': 'budi'},
            'body': 'This is Budi\'s post'
        },
        {
            'author': {'username': 'santi'},
            'body': 'I don\'t know javascript'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)