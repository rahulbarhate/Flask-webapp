import os, sys
from flask import Flask, render_template, request

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("C:\\Users\\asus\\Desktop\\My Programs\\Flask\\Uploading a file\\template\\upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    for file in request.files.getlist("file"):
        target1 = os.path.dirname(sys.argv[0])
        filename = file.filename
        destination = "/".join([target1, filename])
        print(destination)

    return render_template("complete.html")


if __name__ == "__main__":
    app.run(debug = True)
