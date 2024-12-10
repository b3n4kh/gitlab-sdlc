from flask import Flask, render_template, Blueprint, request
from flask.views import MethodView
from flask_htmx import HTMX

from example.filters import example_trigger
from example.config import Config


def is_htmx_request() -> bool:
    return "HX-Request" in request.headers


class Home(MethodView):
    def get(self):
        return render_template("index.html", debug=Config.DEBUG)


class Partial(MethodView):
    def get(self):
        if is_htmx_request():
            return render_template("partial.html", debug=Config.DEBUG)
        return render_template("index.html", debug=Config.DEBUG)


def init(app: Flask):
    HTMX(app)
    app.url_map.strict_slashes = False
    app.jinja_env.filters["example_trigger"] = example_trigger

    home_bp = Blueprint("home", __name__, url_prefix=app.config["APPLICATION_ROOT"])

    home_bp.add_url_rule("/", view_func=Home.as_view("home"))
    home_bp.add_url_rule("/partial", view_func=Partial.as_view("partial"))

    app.register_blueprint(home_bp)
