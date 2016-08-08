# !/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

import rake

# English stopwords
stoppath = "SmartStoplist.txt"

# initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

# run on RAKE on a given text
db = MongoClient("mongodb://192.168.10.9:27017").pdf
for paper in db.papers.find({}, {"_id": 1, "title": 1, "abs": 1}):
    text = ""
    if paper.get("title"):
        text += paper["title"] + "."
    if paper.get("abs"):
        text += paper["abs"]
    if not text:
        continue

    ###
    keywords = rake_object.run(text)
    db.papers.update({"_id": paper["_id"]}, {"$set": {"keywords": [k[0] for k in keywords[0:7]]}})
