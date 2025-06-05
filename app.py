from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model
model = load_model('multi_crop_disease_model.keras')

# Full class names list (replace with your full list)
CLASS_NAMES = [
    'Apple Scab', 'Apple Black Rot', 'Apple Cedar Rust', 'Apple Healthy',
    'Blueberry Healthy', 'Cherry Powdery Mildew', 'Cherry Healthy',
    'Corn Gray Leaf Spot', 'Corn Common Rust', 'Corn Healthy',
    'Grape Black Rot', 'Grape Esca', 'Grape Leaf Blight', 'Grape Healthy',
    'Orange Haunglongbing', 'Peach Bacterial Spot', 'Peach Healthy',
    'Pepper Bacterial Spot', 'Pepper Healthy', 'Potato Early Blight',
    'Potato Late Blight', 'Potato Healthy', 'Raspberry Healthy',
    'Soybean Healthy', 'Squash Powdery Mildew', 'Strawberry Leaf Scorch',
    'Strawberry Healthy', 'Tomato Bacterial Spot', 'Tomato Early Blight',
    'Tomato Late Blight', 'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot',
    'Tomato Spider Mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus',
    'Tomato Mosaic Virus', 'Tomato Healthy'
]

# Route to serve index.html
@app.route('/')
def home():
    return render_template('index.html')

# Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Preprocess image for model prediction
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Provide info about the detected disease
def get_disease_info(disease_name):
    info = {
        "description": "",
        "natural_remedies": [],
        "chemical_treatments": [],
        "prevention": [],
        "resources": []
    }

    if "Early Blight" in disease_name:
        info["description"] = "Early blight is a common fungal disease that affects tomatoes and potatoes. It causes dark spots with concentric rings on leaves."
        info["natural_remedies"] = [
            "Apply neem oil spray every 7-10 days",
            "Use baking soda solution (1 tbsp baking soda + 1 tsp vegetable oil + 1/2 tsp soap in 1 gallon water)",
            "Remove and destroy infected leaves"
        ]
        info["chemical_treatments"] = [
            "Copper-based fungicides (apply every 7-10 days)",
            "Chlorothalonil (apply at first sign of disease)",
            "Mancozeb (apply as protective spray)"
        ]
        info["prevention"] = [
            "Practice crop rotation (don't plant tomatoes/potatoes in same spot for 3 years)",
            "Space plants properly for good air circulation",
            "Water at the base of plants to keep foliage dry",
            "Use mulch to prevent soil splash onto leaves"
        ]
        info["resources"] = [
            {"name": "USDA Early Blight Guide", "url": "https://www.ars.usda.gov/"},
            {"name": "Organic Treatment Research Paper", "url": "https://www.sciencedirect.com/"},
            {"name": "Local Extension Office Contact", "url": "https://nifa.usda.gov/"}
        ]
    # You can add more diseases here similarly

    return info

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            img_array = preprocess_image(filepath)
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class])
            disease_name = CLASS_NAMES[predicted_class]

            response = {
                'disease': disease_name,
                'confidence': confidence
            }

            return jsonify(response)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

        finally:
            if os.path.exists(filepath):
                os.remove(filepath)
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
