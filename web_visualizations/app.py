from flask import Flask, jsonify, redirect, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comparisons")
def compare():
    return render_template("comparisons.html")

@app.route("/data")
def data():
    return render_template("data.html")

if __name__=="__main__":
    app.run(debug=True)