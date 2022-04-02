from flask import Flask,jsonify,request
import csv

from pandas import json_normalize

allArticles = []
likedArticles = []
notlikedArticles = []
didnotWatch = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

app = Flask(__name__)
@app.route('/getArticles')

def getArticles():
    return jsonify({
        "data" : allArticles[0],
        'status' : "success"
    })

@app.route("/likeArticles",methods = ["POST"])

def likeArticles():
    article = allArticles[0]
    allArticles = allArticles[1:]
    likedArticles.append(article)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/notlikeArticles",methods = ["POST"])

def notlikeArticles():
    article = allArticles[0]
    allArticles = allArticles[1:]
    notlikedArticles.append(article)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/notwatchedArticles",methods = ["POST"])

def notwatchedArticles():
    article = allArticles[0]
    allArticles = allArticles[1:]
    didnotWatch.appent(article)
    return jsonify({
        "status" : "success"
    }),201