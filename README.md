# 🎭 Emotion Detection Web App using CNN

## 📌 Project Overview

This project is a **web-based Emotion Detection System** that uses a **Convolutional Neural Network (CNN)** to predict human emotions from images.

The application allows users to:

* Capture an image using a webcam 📷
* Upload an image 📁
* Get real-time emotion predictions 🤖

---

## 🚀 Features

* 🎥 Live camera capture
* 📂 Image upload support
* 🧠 CNN-based emotion prediction
* 🌐 Web interface built with Flask
* 🔗 API-based model integration (Colab + ngrok)

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input Shape: `48 x 48 x 3` (RGB image)
* Output Classes:

  * Angry 😠
  * Disgust 🤢
  * Fear 😨
  * Happy 😄
  * Sad 😢
  * Surprise 😲
  * Neutral 😐

---

## 🏗️ Project Architecture

```
User (Browser)
      ↓
Flask Web App (Local / Render)
      ↓
Colab API (Flask + ngrok)
      ↓
CNN Model (Prediction)
```

---

## 🛠️ Technologies Used

* Python 🐍
* Flask 🌐
* TensorFlow / Keras 🤖
* OpenCV 📷
* NumPy 📊
* HTML, CSS 🎨
* Google Colab ☁️
* ngrok 🔗

---

## 📂 Project Structure

```
emotion-app/
│
├── app.py                 # Main Flask app
├── predict.py             # API connection logic
├── model/
│   └── emotion_model.hdf5 # Trained model
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── uploads/           # Captured/uploaded images
├── requirements.txt
└── README.md
```

---

## 👩‍💻 Author

Adi
BCA Final Year Student

---

## ⭐ Acknowledgment

This project demonstrates a complete **AI system pipeline**, integrating:

* Machine Learning
* Backend Development
* Web Deployment Concepts

---

## 📌 License

This project is for academic and educational purposes.
