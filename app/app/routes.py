from flask import Blueprint, request, jsonify
from .models import Task
from . import db

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/', methods=['POST'], strict_slashes=False)
def create_task():
    data = request.get_json()

    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    title = data.get('title')
    description = data.get('description', '')
    status = data.get('status', 'pending')

    if status not in ['pending', 'completed']:
        return jsonify({'error': 'Status must be either "pending" or "completed"'}), 400

    new_task = Task(title=title, description=description, status=status)
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

@tasks_bp.route('/', methods=['GET'], strict_slashes=False)
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@tasks_bp.route('/<int:task_id>', methods=['GET'], strict_slashes=False)
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict()), 200

@tasks_bp.route('/<int:task_id>', methods=['PUT'], strict_slashes=False)
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Bad request'}), 400

    if 'title' in data:
        if not str(data['title']).strip():
            return jsonify({'error': 'Title cannot be empty'}), 400
        task.title = data['title']
    
    if 'description' in data:
        task.description = data['description']
        
    if 'status' in data:
        if data['status'] not in ['pending', 'completed']:
            return jsonify({'error': 'Status must be either "pending" or "completed"'}), 400
        task.status = data['status']

    db.session.commit()
    return jsonify(task.to_dict()), 200

@tasks_bp.route('/<int:task_id>', methods=['DELETE'], strict_slashes=False)
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200
