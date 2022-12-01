from flask import Flask, jsonify, request, render_template
import json

import app.inference as n

import os

# Create the application instance
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'wav', 'mp3'}


def allowed_file(filename):
    # Check if the file is allowed
    # *.wav or *.mp3
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# API Endpoint: /predict

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print(f"request.files: {request.files}")
    if request.method == "POST":
        # Get the audio file from the request
        audio_file = request.files["file"]
        print(audio_file)

        # Input Checking
        if audio_file is None or audio_file.filename == "":
            return jsonify({"error": "No file was uploaded."})

        if not allowed_file(audio_file.filename):
            return jsonify({"error": "File type not supported."})

        audio_file = request.files['file']

        save_path = os.path.join(os.getcwd(), 'temp.wav')
        audio_file.save(save_path)

        audio_file = save_path

        TheOracle = n.Oracle()
        predictions = TheOracle.get_predictions(audio_file)

        # Descenting order
        predictions = dict(sorted(predictions.items(), key=lambda item: item[1], reverse=True))
        
        # Make predictions pretty
        predictions = {k: str(v) + "%" for k, v in predictions.items()}

        # Convert to JSON
        predictions = json.dumps(predictions, indent=4)
        
        
        print(f"predictions: {predictions}")
        return render_template('predictions.html', confidence=predictions)

