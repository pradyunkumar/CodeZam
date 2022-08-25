import json
import os
from flask import Flask, render_template, request, jsonify
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

#@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
#   if request.method == 'POST':
#      f = request.files['file']
#      f.save(secure_filename(f.filename))
#    #   return predict(f)
#      return prediction(f)

#def prediction(file):
#    result = str(format_output(predict(secure_filename(file.filename))))
#    flash(result)
#    print(result)
#    return render_template("/result.html")

@app.route("/receive", methods=['POST'])
def form():
    file = request.files['file']
    file.save(secure_filename(file.filename))
    print(file)

    # with open(os.path.abspath(f'{file.filename}'), 'wb') as f:
    #     f.write(file.getvalue())

    result = str(format_output(predict(secure_filename(file.filename))))
    os.remove(secure_filename(file.filename))

    # filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    # f.save(filepath)

    # Jump back to the beginning of the file.
    # f.seek(0)
    
    # # Read the audio data again.
    # data, samplerate = soundfile.read(filename)
    # with io.BytesIO() as fio:
    #     soundfile.write(
    #         fio, 
    #         data, 
    #         samplerate=samplerate, 
    #         subtype='PCM_16', 
    #         format='wav'
    #     )
    #     data = fio.getvalue()

    #response = jsonify("File received and saved!")
    #response.headers.add('Access-Control-Allow-Origin', '*')

    result = jsonify(result)
    return result
    
def format_output(res):
    results = res['results']
    results.sort(key=lambda x: x['hashes_matched_in_input'], reverse=True)
    return str({i: res['results'][i]['song_name'] for i in range(len(res['results']))})
    # return res

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
