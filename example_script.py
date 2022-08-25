import json
import sys
sys.path.append("/Users/prady/Documents/Programming/codezam_connect/dejavu")
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
# from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer
from dejavu import Dejavu

# load config from a JSON file (or anything outputting a python dictionary)
# with open("dejavu.cnf.SAMPLE") as f:
#     config = json.load(f)

config = {
    "database": {
        "host": "db",
        "user": "postgres",
        "password": "password",
        "database": "dejavu",
        "port": 5432,
    },
    "database_type": "postgres"
}

def predict(file):
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("test", [".wav"])

    # Recognize audio from a file
    results = djv.recognize(FileRecognizer, file)
    print(f"From file we recognized: {results}\n")

    # Or recognize audio from your microphone for `secs` seconds
    # secs = 5
    # results = djv.recognize(MicrophoneRecognizer, seconds=secs)
    # if results is None:
    #     return "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
    # else:
    #     return f"From mic with {secs} seconds we recognized: {results}\n"
    return results

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("test", [".wav"])

    # Recognize audio from a file
    results = djv.recognize(FileRecognizer, "mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    print(f"From file we recognized: {results}\n")

    # Or recognize audio from your microphone for `secs` seconds
    # secs = 5
    # results = djv.recognize(MicrophoneRecognizer, seconds=secs)
    # if results is None:
    #     print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
    # else:
    #     print(f"From mic with {secs} seconds we recognized: {results}\n")

    # Or use a recognizer without the shortcut, in anyway you would like
    recognizer = FileRecognizer(djv)
    results = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    print(f"No shortcut, we recognized: {results}\n")
