# __author__ = 'Atria'
#
# from flask import Flask, render_template
#
# app = Flask(__name__)  # name
#
#
# @app.route('/')
# def hello_method():
#     return render_template('library.html')
#
#
# if __name__ == '__main__':
#     app.run(port=4955)

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, './html/library.html', {'': ''})

# print('test 123')
