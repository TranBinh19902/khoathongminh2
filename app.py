from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(UPLOAD_FOLDER, f"img_{now}.jpg")
    with open(file_path, 'wb') as f:
        f.write(request.data)
    print(f"[INFO] Saved {file_path}")
    return "Image received", 200
