#! /usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import ExampleForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET','POST'])
def about():
    form = ExampleForm()
    if form.validate_on_submit():
        u = form.username.data
        p = form.password.data
        print(u,p)
    return render_template('about.html', form=form)

if __name__=='__main__':
    app.run(debug=True)