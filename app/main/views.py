from .import main
from flask import render_template

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/mentors')
def mentors():
    return render_template('mentors.html')  