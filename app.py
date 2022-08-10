import json
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from example_script import predict

# Create App
app = Flask(__name__)

# Select Route
@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/about-us')
@app.route('/about-us.html')
def about_us():
    return render_template("about-us.html")

@app.route('/more')
@app.route('/more.html')
def more():
    return render_template("more.html")

@app.route('/works')
@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
    #   return predict(f)
      return prediction(f)

def prediction(file):
    print(predict(secure_filename(file.filename)))
    return redirect('index.html')

# def predict(file):
#     with open("/Users/prady/Documents/Programming/codezam_connect/dejavu/dejavu.cnf.SAMPLE") as f:
#         config = json.load(f)
#     djv = Dejavu(config)

#     # Fingerprint all the mp3's in the directory we give it
#     djv.fingerprint_directory("test", [".wav"])

#     # Recognize audio from a file
#     results = djv.recognize(FileRecognizer, file.name)
#     print(f"From file we recognized: {results}\n")

#     # Or recognize audio from your microphone for `secs` seconds
#     secs = 5
#     results = djv.recognize(MicrophoneRecognizer, seconds=secs)
#     if results is None:
#         return "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
#     else:
#         return f"From mic with {secs} seconds we recognized: {results}\n"

		
# import os
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)