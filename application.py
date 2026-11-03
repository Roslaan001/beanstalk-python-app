import os
import platform
import sys
import time
from datetime import datetime
from flask import Flask, render_template, jsonify, request

# Elastic Beanstalk looks for an 'application' callable in application.py
application = Flask(__name__)

# Track start time for uptime calculation
START_TIME = time.time()

# In-memory storage for sample interactive notes/tasks
notes_db = [
    {
        "id": 1,
        "text": "AWS Elastic Beanstalk environment configured",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 2,
        "text": "Flask WSGI application ready for deployment",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
]


@application.route('/')
def index():
    uptime_seconds = int(time.time() - START_TIME)
    system_info = {
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "uptime": f"{uptime_seconds}s",
        "env": os.environ.get("FLASK_ENV", "production")
    }
    return render_template('index.html', info=system_info)


@application.route('/health')
def health():
    uptime_seconds = int(time.time() - START_TIME)
    return jsonify({
        "status": "healthy",
        "uptime_seconds": uptime_seconds,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "python_version": sys.version.split()[0]
    })


@application.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        text = data.get('text', '').strip()
        if not text:
            return jsonify({"error": "Note text cannot be empty"}), 400

        new_note = {
            "id": len(notes_db) + 1,
            "text": text,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        notes_db.append(new_note)
        return jsonify(new_note), 201

    return jsonify(notes_db)


@application.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes_db
    notes_db = [n for n in notes_db if n['id'] != note_id]
    return jsonify({"success": True})


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
