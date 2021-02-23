from flask import render_template, request, url_for, redirect, abort, make_response
from flask.wrappers import Response
from postcard import app
from .functions import *

@app.route('/')
def index() -> str:
    return render_template("index.html")

# 就现在的优化而言，不推荐使用前两个，
# 毕竟只是简单地挖掉了部分，
# 没有修改路径和 viewbox
@app.route('/greeting')
def greeting() -> Response:
    # 任何 url 参数将被忽略
    ip = request.access_route[0]
    svg = render_template(
        "greeting.svg",
        user_agent=request.user_agent,
        date=today(),
        ip=ip,
        geo=getCity(ip),
        c=request.args,
    )
    resp = make_response(svg)
    resp.mimetype = "image/svg+xml"
    return resp

@app.route('/contact')
def contact() -> Response:
    # https://www.jianshu.com/p/3c757e21e897
    svg =  render_template(
        "contact.svg",
        c=request.args,
    )
    resp = make_response(svg)
    resp.mimetype = "image/svg+xml"
    return resp

@app.route('/postcard')
def postcard() -> Response:
    ip = request.access_route[0]
    # https://www.jianshu.com/p/3c757e21e897
    svg =  render_template(
        "postcard.svg",
        user_agent=request.user_agent,
        date=today(),
        ip=ip,
        c=request.args,
        geo=getCity(ip),
    )
    resp = make_response(svg)
    resp.mimetype = "image/svg+xml"
    return resp

# 彩蛋不能没有（即使懒得优化
@app.route('/teapot')
def egg():
    abort(418)
