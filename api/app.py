#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Nov 8, 2019

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Flask-based RESTful API for KBQA on DBpedia
'''
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from request import KBQA

class KBQAPI(Resource):
    def setup(self):
        self.service = KBQA()

    def get(self):
        question = request.args.get('question', type=str)
        top_n = request.args.get('top_n', default=3, type=int)
        answers = self.service.request(question, top_n, verbose=False)
        return jsonify({'answers': answers})

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    kbqa = KBQAPI()
    kbqa.setup()
    api.add_resource(kbqa, '/')
    app.run(debug=True)
