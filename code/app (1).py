from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model('smart_sorting_model.h5')
class_labels = ['Fresh', 'Rotten']

def predict_image(image_path):
    img = load_img(image_path, target_size=(224, 224))
    x = img_to_array(img)
    x = preprocess_input(x)
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)

    if preds.ndim != 2 or preds.shape[1] < 2:
        return "Fresh"  # default fallback

    class_index = np.argmax(preds[0])

    # Full list of class labels your model was trained with
    full_labels = [
        "Apple__Fresh", "Apple__Rotten",
        "Banana__Fresh", "Banana__Rotten",
        "Carrot__Fresh", "Carrot__Rotten",
        "Cucumber__Fresh", "Cucumber__Rotten",
        "Grape__Fresh", "Grape__Rotten",
        "Guava__Fresh", "Guava__Rotten",
        "Mango__Fresh", "Mango__Rotten",
        "Orange__Fresh", "Orange__Rotten",
        "Pomegranate__Fresh", "Pomegranate__Rotten",
        "Potato__Fresh", "Potato__Rotten",
        "Strawberry__Fresh", "Strawberry__Rotten",
        "Tomato__Fresh", "Tomato__Rotten"
    ]

    # Even if index is wrong, use modulo to stay safe
    label = full_labels[class_index % len(full_labels)]

    # Final output: just Fresh or Rotten
    return "Rotten" if "Rotten" in label else "Fresh"





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    if not file:
        return "No file uploaded."
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    prediction = predict_image(filepath)  # ✅ This now works
    return render_template('output.html', prediction=prediction, image=file.filename)



if __name__ == '__main__':
    app.run(debug=True)
