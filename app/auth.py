from flask import Blueprint, render_template, redirect, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .extensions import login_maneger
from . import db

auth = Blueprint('auth',  __name__)

@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():

    if request.method == 'POST':
        # Getting data entered by user in the SignUp form
        username = request.form.get('username')
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('pwd')

        user = User.query.filter_by(email=email).first() # check if the user already exists with the given name

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('User already exist with the given email, try another email or login with the entered email')
            return redirect('/signup')

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        else : 
            new_user = User(username=username, email=email, name=name, password=generate_password_hash(password))

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            flash('User added successfully. Now you can login')
            return redirect('/')

    return render_template('auth/signup.html')

@auth.route('/login', methods=["POST", "GET"])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
    
        user = User.query.filter_by(username=username).first() # searching for the user with the given username

        if user: # if user exists then validating the password and logging-In the user
            if check_password_hash(user.password, password):
                login_user(user, remember=False)
                return redirect('/')

            else: # if password is wrong then asking to retry 
                flash('Wrong Password. Please try again')
                return redirect('/login')

        else: 
            flash('User Not Found')
            return redirect('/login')
    
    return render_template('auth/login.html')

# Loggin-Out the user
@auth.route('/logout')
@login_required
def logut():
    logout_user()
    
    return redirect('/')

@login_maneger.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()