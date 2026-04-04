from flask import Flask, render_template, request
import os
import base64
from predict import predict_emotion

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 🔥 Ensure upload folder exists (IMPORTANT FIX)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    emotion = None
    file_path = None

    if request.method == 'POST':

        # 🔹 Camera image (base64)
        if request.form.get('image_data'):
            image_data = request.form['image_data']
            image_data = image_data.split(",")[1]

            file_path = os.path.join(UPLOAD_FOLDER, 'capture.png')

            with open(file_path, "wb") as f:
                f.write(base64.b64decode(image_data))

            emotion = predict_emotion(file_path)

        # 🔹 File upload
        elif 'image' in request.files:
            file = request.files['image']
            if file:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)

                emotion = predict_emotion(file_path)

    return render_template('index.html', emotion=emotion, file_path=file_path)


# 🔥 IMPORTANT FOR DEPLOYMENT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
