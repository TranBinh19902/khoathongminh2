from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server is live 🎉', 200

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # xử lý ảnh ở đây
    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
