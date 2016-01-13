from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from human.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(256))
    createtime = db.Column(db.DateTime)
    imageses = db.relationship('Images', backref='user', lazy='dynamic')
    videoses = db.relationship('Videos', backref='user', lazy='dynamic')

    def __init__(self,name,password,createtime):
        self.name = name
        self.password = password
        self.createtime = createtime

class Images(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256))
    url = db.Column(db.String(512))
    description = db.Column(db.String(2048))
    createtime = db.Column(db.DateTime)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,title,url,description,createtime,author):
        self.title = title
        self.url = url
        self.description = description
        self.createtime = createtime
        self.author = author

class Videos(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(128))
    fixurl = db.Column(db.String(128))
    description = db.Column(db.String(2048))
    createtime = db.Column(db.DateTime)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,title,fixurl,description,createtime,author):
        self.title = title
        self.fixurl = fixurl
        self.description = description
        self.createtime = createtime
        self.author = author

class Sitecolumns(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(128))
    url = db.Column(db.String(128))
    description = db.Column(db.String(512))
    createtime = db.Column(db.DateTime)
    createuser = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,name,url,description,createuser,createtime):
        self.name = name
        self.url = url
        self.createtime = createtime
        self.description = description
        self.createuser = createuser

