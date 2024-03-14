from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        text = extract_text(file)
        return text

def extract_text(image):
    # Perform OCR
    text = pytesseract.image_to_string(Image.open(image))
    return text

if __name__ == '__main__':
    app.run(debug=True)
