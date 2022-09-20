from flask import Flask
app = Flask(__name__)
@app.route("/takehome")
def home():
    return "A OK"