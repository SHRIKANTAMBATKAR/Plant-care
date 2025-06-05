# 🌿 Multi-Disease Multi-Crop Detection System

A Deep Learning-based web application to **detect multiple diseases in multiple crops** using computer vision. Designed especially for **farmers, agronomists, and researchers**, the system allows you to upload a plant leaf image and get instant disease predictions, treatment tips, and expert advisory information.


## 📖 About the Project

This project uses **Convolutional Neural Networks (CNNs)** with the **PlantVillage dataset** to train a crop disease detection model. It’s integrated into a **Flask web app** so users can upload plant leaf images and view the diagnosis instantly. The application is built to be simple, responsive, and mobile-friendly for real-world use by farmers.

## ✅ Features

- 🖼️ Upload crop/leaf images (JPEG, PNG)
- 🤖 Predict plant diseases with confidence score
- 📋 Disease details including description & symptoms
- 💊 Natural & chemical treatment suggestions
- 🧪 Soil and crop advisory info
- 📱 Fully responsive design (mobile & desktop)
- 🔁 Easy to run locally (Flask + TensorFlow + HTML/CSS)

---

## 📁 Project preview
![Screenshot 2025-06-06 012606](https://github.com/user-attachments/assets/961f1883-df98-4a45-8ee2-9b693943b2da)


## 🛠️ How to Install and Run in VS Code

### ✅ Prerequisites

- Python 3.8+
- VS Code installed
- Git installed (optional)
- A GPU is recommended but not required

### 📥 Step-by-Step Setup in Visual Studio Code

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/multi-crop-disease-detection.git
   cd multi-crop-disease-detection
Open in VS Code

Open VS Code

Go to File > Open Folder... and select the cloned project

Create a Virtual Environment
Open the terminal in VS Code:

python -m venv venv
Activate the Virtual Environment

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate
Install Required Python Packages
pip install -r requirements.txt

If requirements.txt is not present, install manually:
pip install flask tensorflow pillow numpy flask-cors
Make Sure the Model File Exists
Ensure multi_crop_disease_model.keras is in the root folder.

Run the Flask App
python app.py
Open in Browser
Visit http://127.0.0.1:5000 to view your app.
