# PashuSuchak AI - Backend Server
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from model import predict_breed

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
SPRITE_FOLDER = 'text_sprites'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SPRITE_FOLDER'] = SPRITE_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SPRITE_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    """
    Analyze an uploaded image to identify the animal breed
    """
    # Check if the post request has the file part
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
    
    file = request.files['image']
    
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Call the model to predict the breed
        result = predict_breed(file_path)
        
        # Create a relative URL for the sprite
        if 'sprite_path' in result and result['sprite_path']:
            sprite_filename = os.path.basename(result['sprite_path'])
            result['sprite_url'] = f"/api/sprites/{sprite_filename}"
        
        return jsonify(result)
    
    return jsonify({"error": "File type not allowed"}), 400

@app.route('/api/sprites/<filename>', methods=['GET'])
def get_sprite(filename):
    """
    Serve sprite text files
    """
    sprite_path = os.path.join(os.path.dirname(__file__), 'text_sprites', filename)
    if os.path.exists(sprite_path):
        return send_file(sprite_path, mimetype='text/plain')
    return jsonify({"error": "Sprite not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)