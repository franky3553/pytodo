## /1/ Import flask ando some libraries

from flask import Flask, render_template, request, redirect, url_for

## /4/ Import sqlalchemy for DB

from flask_sqlalchemy import SQLAlchemy

## /2/ Create app instance 

app = Flask(__name__)

## /5/ Set sqlalchemy congfiguartion variables

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) ## "db" now is "SQLAlchemy(app)"


## /3/ Def home function 

@app.get("/")
def home():
	todo_list = db.session.query(Todo).all()
	return render_template("base.html", todo_list=todo_list)