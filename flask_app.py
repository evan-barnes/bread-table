from flask import Flask
import breadtable

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return breadtable.get_random_bread()
