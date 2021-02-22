from flask import render_template, request, url_for, redirect, abort
from postcard import app
from .functions import *

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
    return render_template(
        "postcard.svg",
        user_agent=request.user_agent,
        date=today(),
        ip=request.access_route[0],
        c=request.args
    )
