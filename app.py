from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
known_folder = 'known_faces'
os.makedirs(known_folder, exist_ok=True)

capture_flag = False
person_name = None

@app.route('/')
def index():
   return render_template('cmsn.html')

@app.route('/trigger-capture', methods=['POST'])
def trigger_capture():
    global capture_flag, person_name
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Thiếu tên'}), 400
    person_name = data['name']
    capture_flag = True
    return jsonify({'status': 'ok'})

@app.route('/capture-request', methods=['GET'])
def capture_request():
    global capture_flag, person_name
    if capture_flag:
        capture_flag = False
        return person_name
    return 'no'

@app.route('/register-face', methods=['POST'])
def register_face():
    if 'image' not in request.files or 'name' not in request.form:
        return jsonify({'error': 'Thiếu image hoặc name'}), 400
    img = request.files['image']
    name = request.form['name'].strip().lower().replace(' ', '_')
    filename = f"{name}_{datetime.now():%Y%m%d_%H%M%S}.jpg"
    path = os.path.join(known_folder, filename)
    img.save(path)
    return jsonify({'status': 'saved', 'filename': filename})
