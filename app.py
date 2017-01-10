#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (
    Flask,
    request,
    jsonify,
    abort
)

#################
# configuration #
#################

app = Flask(__name__)
import logging

app.logger.setLevel(logging.INFO)

##########
# routes #
##########

@app.route('/<uid>')
def index(uid):
    return "ok {0}".format(uid)

if __name__ == '__main__':
    app.run(debug=True, port=5123, host="0.0.0.0")

