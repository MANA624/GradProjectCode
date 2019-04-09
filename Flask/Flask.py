from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from jinja2.exceptions import UndefinedError

app = Flask(__name__)
app.debug = True
client = MongoClient('localhost')
db = client.ooad
tutorialsdb = db.tutorials
threads = db.threads
responses = db.responses


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/tutorials')
def tutorials():
    tuts = []
    for tut in tutorialsdb.find():
        tuts.append(tut)
    return render_template("tutorials.html", tutorials=tuts)


@app.route('/tutorials/<tutorial_id>')
def tutorial(tutorial_id):
    try:
        tut = tutorialsdb.find_one({"_id": ObjectId(tutorial_id)})
        if not tut:
            raise UndefinedError
        tut["num_views"] += 1
        tutorialsdb.update({"_id": tut["_id"]}, tut)
    except UndefinedError:
        return "You found the wrong page!"
    return render_template("tutorial.html", tutorial=tut)


@app.route('/forum')
def forum():
    posts = []
    for post in threads.find():
        posts.append(post)
    print(posts)
    return render_template("forums.html", threads=posts)


@app.route('/forum/<thread_id>')
def see_thread(thread_id):
    try:
        thread = threads.find_one({"_id": ObjectId(thread_id)})
        if not thread:
            raise UndefinedError
        response_list = []
        for response in responses.find({"thread": ObjectId(thread_id)}):
            response_list.append(response)
    except UndefinedError:
        return "You found the wrong page!"
    print(response_list)
    print(thread)
    return render_template("thread.html", thread=thread, posts=response_list)

if __name__ == '__main__':
    app.run()
