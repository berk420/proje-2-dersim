from flask import Flask, render_template, request
import re
import requests
from bs4 import BeautifulSoup
from flashtext import KeywordProcessor
from googlesearch import search




app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])




def getvalue():
    name=request.form['name']
    path="C:/Users/berk/Desktop/PROJE/metin.txt"
    dosya = open(path, 'w')
    dosya.write(name)
    dosya.close()

    #doyadan çıktıyı okuyucaz buraya yazıcaz
    pathiki="C:/Users/berk/Desktop/PROJE/text.txt"
    dosyaiki=open(pathiki,"r")
    for satir in dosyaiki :
         text=satir
    return render_template('pass.html', n=text)


if __name__ == '__main__':
    app.run(debug=True)

