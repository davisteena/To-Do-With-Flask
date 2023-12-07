from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    task_priority = request.form['task_priority']

    task = {
        'name': task_name,
        'description': task_description,
        'priority': task_priority,
        'created_at': datetime.now(),
        'completed_at': None
    }

    tasks.insert(0, task)
    return redirect(url_for('index'))


@app.route('/complete_task/<int:index>')
def complete_task(index):
    tasks[index]['completed_at'] = datetime.now()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
