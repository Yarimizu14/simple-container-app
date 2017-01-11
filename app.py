#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (
    Flask,
    request,
    jsonify,
    abort
)

from flask.ext.sqlalchemy import SQLAlchemy

import os
import json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

#################
# configuration #
#################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
import models

import logging
app.logger.setLevel(logging.INFO)

##########
# routes #
##########

@app.route('/')
def index():
    return "ok"

@app.route('/messages', methods=['GET'])
def list():
    try:
        l = models.Messages.query.all()
        msgs = [f.to_dict() for f in l]
        return jsonify(msg=msgs)
    except Exception as e:
        app.logger.error("{}".format(type(e)))
        return 'Internal Server Error', 500


@app.route('/messages/<message>', methods=['POST'])
def add(message):
    # get url
    f = models.Messages(message)
    db.session.add(f)

    try:
        db.session.commit()
    except IntegrityError:
        app.logger.debug("duplicate file, skipping")
    except Exception as e:
        app.logger.warning("{}".format(type(e)))
    return jsonify(msg=message)


if __name__ == '__main__':
    app.run(debug=True, port=5123, host="0.0.0.0")

