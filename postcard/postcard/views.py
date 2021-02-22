from flask import render_template, request, url_for, redirect, flash
from postcard import app

@app.route('/')
def index() -> str:
    return render_template("index.html")

@app.route('/greeting.svg')
def greeting() -> str:
    pass

@app.route('/contact.svg')
def contact() -> str:
    pass

@app.route('/postcard.svg')
def postcard() -> str:
    pass
