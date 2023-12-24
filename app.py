from flask import Flask, render_template, request, url_for, redirect 
from src import huffman_encoder
# from src import tree_constructor
# from src import utils

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
