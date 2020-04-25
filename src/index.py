from flask import Flask,request,render_template
from kmp import *
from bm import *
from regx import *
from main import *
import re
app = Flask(__name__)


@app.route("/bm", methods=['POST'])
def showBm():
    naskahList = request.files.getlist('naskah')
    pattern = request.form['pattern']
    result = {}
    for item in naskahList:
        naskah = item.read().decode()
        result[item.filename] = readBm(naskah,pattern)
    return result

@app.route("/KMP",methods=['POST'])
def showKMP():
    naskahList = request.files.getlist('naskah')
    pattern = request.form['pattern']
    result = {}
    for item in naskahList:
        naskah = item.read().decode()
        result[item.filename] = readKMP(naskah,pattern)
    return result

@app.route("/re",methods=['POST'])
def showRegx():
    naskahList = request.files.getlist('naskah')
    pattern = request.form['pattern']
    result = {}
    for item in naskahList:
        naskah = item.read().decode()
        result[item.filename] = readRegx(naskah,pattern)
    return result

@app.route("/about",methods=['POST'])
def hewwo():
    return "nim : 13518116"

@app.route("/",methods =['GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()