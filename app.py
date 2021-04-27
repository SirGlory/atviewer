# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, Markup, jsonify
from data_check import DataCheck
from flask_wtf import FlaskForm, CSRFProtect
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, Length
from wtforms.fields import *
from werkzeug.utils import redirect
from scrape_last_photos import PhotoUrls

app = Flask(__name__)
app.secret_key = '420dev710'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# set default button style and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'
# app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'  # uncomment this line to test bootswatch theme

bootstrap = Bootstrap(app)


# db = SQLAlchemy(app)
# csrf = CSRFProtect(app)


class HandleForm(FlaskForm):
    handle = StringField(render_kw={'placeholder': 'Enter Instagram Handle'})
    submit = SubmitField("Generate Map")


@app.route('/')
def index():
    form = HandleForm()
    return render_template('index.html', form=form)


@app.route('/photos', methods=['POST'])
def photogen():
    handle_form = HandleForm(request.form)
    data = str(handle_form.handle.data)
    print(data)
    handle = data.replace("@", "").replace(" ", "")  # accounts for @ or space in search field
    linkss = PhotoUrls(handle=handle).photo_links()
    url = linkss[0]
    links = linkss[1:-1]
    return render_template('photos.html', images=links, first_image=url)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/at_viewer', methods=['GET'])
def at_viewer():
    return redirect("https://atmapper.herokuapp.com/")


@app.route('/explore', methods=['GET', 'POST'])
def explore():
    return render_template('explore.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
