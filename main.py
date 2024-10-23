from flask import Flask, render_template
from flask.views import View

class basic(View):
    def __init__(self):
        