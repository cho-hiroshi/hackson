# coding: utf-8
from argparse import ArgumentParser
from flask import Flask, render_template, request



app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", entry=None)


@app.route("/result", methods=["POST"])
def result():
    query = request.form["query"]
    entry = {"query": query}
    return render_template("result.html", entry=entry)


arg_parser = ArgumentParser(
    usage='Usage: python ' + __file__ + ' [--host <address>] [--port <port>] [--debug]'
)
arg_parser.add_argument('--host', default="0.0.0.0", help='host')
arg_parser.add_argument('-p', '--port', default=80, help='port')
arg_parser.add_argument('-d', '--debug', default=True, help='debug')
args = arg_parser.parse_args()

app.run(host=args.host, port=args.port, debug=args.debug)
