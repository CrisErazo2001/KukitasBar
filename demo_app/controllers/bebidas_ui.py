from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app

from flask_bcrypt import Bcrypt
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
        return redirect('/bebida')


