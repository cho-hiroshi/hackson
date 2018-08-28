# coding: utf-8
from argparse import ArgumentParser
from flask import Flask, render_template, request
from retrieve import Solr



app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", entry=None)


@app.route("/result", methods=["POST"])
def result():
    query = request.form["query"]

    # retrieve
    # TODO: エンドポイントを埋める
    solr = Solr('endpoint')
    # result_triples = solr.retrive(query)
    result_triples = solr.mock_retrive(query)
    entry = {"query": query, 'result': result_triples}
    return render_template("result.html", entry=entry)


if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--host <address>] [--port <port>] [--debug]'
    )
    arg_parser.add_argument('--host', default="0.0.0.0", help='host')
    arg_parser.add_argument('-p', '--port', default=80, help='port')
    arg_parser.add_argument('-d', '--debug', default=True, help='debug')
    args = arg_parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
