import sys

from flask import Flask, redirect
from utils import configure
from utils import configure_backend
from utils import configure_cache

app = Flask(__name__)

conf = configure("conf.yml")
backend = configure_backend(conf)
if not backend:
    print("backend is not configured")
    sys.exit(1)
urls = configure_cache(conf, backend)


@app.route('/<string:short>', methods=['GET'])
def hello_world(short):
    if short not in urls:
        return "NOT FOUND", 404
    return redirect(urls.get(short))


@app.errorhandler(404)
def not_found():
    return "NOT FOUND", 404
