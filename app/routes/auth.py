from flask import session, redirect, render_template, url_for,Blueprint, flash, request
from app import db
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.view_tasks'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_data = User.query.filter_by(username=username).first()

        if user_data and check_password_hash(user_data.password, password):
            flash('Login Successful', 'Success')
            login_user(user_data, remember=True)
            return redirect(url_for('tasks.view_tasks'))

        else:
            flash('Invalid Credentials', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/', methods = ["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.view_tasks'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_data = User.query.filter_by(username=username).first()
        
        if user_data:
            flash("User already exists, try logging in.")
            return redirect(url_for("auth.login"))
        elif len(username) < 2:
            flash("Username should be atleast 2 characters long. Try again", "Error")
        elif len(password) < 6:
            flash("Password should be atleast 6 characters long. Try again", "Error")
        else:
            new_user = User(username = username, password = generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Registered successfully.', 'Success')
            return redirect(url_for("tasks.view_tasks"))
        
    return render_template("register.html")

