from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user
from . import db
from .models import User, Hostel, Room, Booking
from .forms import LoginForm, BookingForm
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
