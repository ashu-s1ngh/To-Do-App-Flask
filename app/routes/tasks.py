from flask import url_for, redirect, render_template, request, session, Blueprint, flash
from app import db
from app.models import Task
from flask_login import current_user, login_required


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks')
@login_required
def view_tasks():
    tasks = Task.query.filter_by(user_id = current_user.id).all()
    return render_template('tasks.html', tasks = tasks)

@tasks_bp.route('/add', methods = ['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title = title, status = 'Pending', user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'Success')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
@login_required
def toggle_status(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'

        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods = ['POST'])
@login_required
def clear_task():
    Task.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('tasks.view_tasks'))