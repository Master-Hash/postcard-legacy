from flask import render_template, request, redirect, abort, make_response
from flask.wrappers import Response
from postcard import app
from .functions import *
import asyncio

@app.route('/')
def index():
    return redirect("https://github.com/Master-Hash/postcard", 301)

# 就现在的优化而言，不推荐使用前两个，
# 毕竟只是简单地挖掉了部分，
# 没有修改路径和 viewbox
# @app.route('/greeting')
# def greeting() -> Response:
#     # 任何 url 参数将被忽略
#     ip = request.access_route[0]
#     svg = render_template(
#         "greeting.svg",
#         user_agent=request.user_agent,
#         date=today(),
#         ip=ip,
#         geo=getCity(ip),
#         c=request.args,
#     )
#     resp = make_response(svg)
#     resp.mimetype = "image/svg+xml"
#     return resp

# 如果真的只需要留联系方式，为什么要用动态名片呢？
# @app.route('/contact')
# def contact() -> Response:
#     # https://www.jianshu.com/p/3c757e21e897
#     svg =  render_template(
#         "contact.svg",
#         c=request.args,
#     )
#     resp = make_response(svg)
#     resp.mimetype = "image/svg+xml"
#     return resp

# @app.route('/postcard')
# def postcard() -> Response:
#     ip = request.access_route[0]
#     # https://www.jianshu.com/p/3c757e21e897
#     svg = render_template(
#         "postcard.svg",
#         user_agent=request.user_agent,
#         date=today(),
#         ip=ip,
#         c=request.args,
#         geo=getCity(ip),
#     )
#     resp = make_response(svg)
#     resp.mimetype = "image/svg+xml"
#     return resp

@app.route('/teapot')
def egg():
    abort(418)

# @app.route('/debug/<int:code>')
# def tmp(code: int):
#     abort(code)

# 算了，难得整了
# @admin.errorhandler(404)
# def error_404(error):
#     return render_template("404.html", 404)

# @admin.errorhandler(500)
# def error_500(error):
#     return render_template("500.html", 500)

# @admin.errorhandler(400)
# def error_400(error):
#     return render_template("400.html", 400)

@app.route('/api')
def api() -> Response:
    _ip = request.access_route[0]
    _icons = {i:request.args[i] for i in request.args if i in icons}
    _items = asyncio.run(getSocial(_icons))

    if "img" in request.args and (_img:=request.args["img"]) in ("in", "ex"):
        if "src" in request.args:
            _src = request.args["src"]
        else:
            abort(400)
    else:
        _img = _src = None

    if _img == "in":
        _data = fileToBase64(_src)
    elif _img == "ex":
        _data = hrefToBase64(_src)
    else:
        _data = None

    _c = {i: (request.args[i] if i in request.args else required_param[i]) for i in required_param}

    svg = render_template(
        "api.svg",
        user_agent=request.user_agent,
        date=today(),
        ip=_ip,
        geo=getCity(_ip),
        items=_items,
        img=_img,
        data=_data,
        c=_c,
    )
    resp = make_response(svg)
    resp.mimetype = "image/svg+xml"
    return resp
