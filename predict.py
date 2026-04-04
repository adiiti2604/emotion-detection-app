import cv2
import numpy as np
from keras.models import load_model

# model = load_model('model/emotion_model.hdf5')
model = None
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# def predict_emotion(img_path):
#     image = cv2.imread(img_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     face_cascade = cv2.CascadeClassifier(
#         cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
#     )

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         roi = gray[y:y+h, x:x+w]
#         roi = cv2.resize(roi, (48, 48))
#         roi = roi / 255.0
#         roi = np.reshape(roi, (1, 48, 48, 1))

#         prediction = model.predict(roi)
#         return emotion_labels[np.argmax(prediction)]

#     return "No Face Detected"

def predict_emotion(img_path):
    return "Model not loaded yet 😄"