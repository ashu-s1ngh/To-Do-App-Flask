from flask import session, redirect, render_template, url_for,Blueprint, flash, request
from app import db
from app.models import User


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ["GET", "POST"])
def login():
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_data = User.query.filter_by(username=username).first()

        if user_data and password == user_data.password:
            session['user'] = username
            flash('Login Successful', 'Success')
            return redirect(url_for('tasks.view_tasks'))

        else:
            flash('Invalid Credentials', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged Out', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/', methods = ["GET", "POST"])
def register():
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_data = User.query.filter_by(username=username).first()
        
        if not user_data:
            new_user = User(username = username, password = password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully, you can login now.', 'Success')
        else:
            flash("User already exists, try logging in.")
            return redirect(url_for("auth.login"))
        
    return render_template("register.html")

