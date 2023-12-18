from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
#    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('home.html')

@app.route('/about')
def about():
#    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('about.html')

@app.route('/numbers')
def numbers():
    return render_template('numbers.html')

@app.route('/poetry') #/<int:post_id>')
def poetry():

    return render_template('poetry.html')
@app.route('/sport')
def sport():

    return render_template('sport.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
