## /1/ Import flask ando some libraries

from flask import Flask, render_template, request, redirect, url_for



## /2/ Create app instance 

app = Flask(__name__)


## /3/ Def home function 

@app.get("/")
def home():
	todo_list = db.session.query(Todo).all()
	return render_template("base.html", todo_list=todo_list)