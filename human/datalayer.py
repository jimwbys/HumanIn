from model import User,Images,Sitecolumns,Videos
import md5
import datetime
from human.extensions import db


def add_newuser(name,password):
    newuser = User(name,md5.md5(password).hexdigest(),datetime.datetime.now())
    current = User.query.filter_by(name=newuser.name).first()
    if current is None:
        db.session.add(newuser)
        db.session.commit()

def is_username_available(name):
    current = User.query.filter_by(name=name).first()
    if current is None:
        return True
    else:
        return False

def delete_user(name):
    user = User.query.filter_by(name=name).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()

def get_user(name):
    user = User.query.filter_by(name=name).first()
    return user

def check_user(src_password,det_password):
     if src_password == md5.md5(det_password).hexdigest():
        return True
     else:
        return False

def update_user(oldname,newname,newpassword):
    user = User.query.filter_by(name=oldname).first()
    current = User.query.filter_by(name=newuser.name).first()
    if current is None:
        user.name = newname
        user.password = newpassword
        db.session.commit()

def add_sitecolumns(name,url,description,userid):
    sitecolumns = Sitecolumns(name,url,description,userid,datetime.datetime.now())
    current = Sitecolumns.query.filter_by(name=name).first()
    if current is None:
        db.session.add(sitecolumns)
        db.session.commit()

def delete_sitecolumns(name):
    current = Sitecolumns.query.filter_by(name=name).first()
    if current is None:
        db.session.delete(current)
        db.session.commit()

def update_sitecolumns(oldname,newname,newurl,newdescription):
    old = Sitecolumns.query.filter_by(name=oldname).first()
    if old is not None:
        current = Sitecolumns.query.filter_by(name=newname).first()
        if current is None:
            old.name = newname
            old.url = newurl
            old.description = newdescription
            db.session.commit()

def get_sitecolumns():
    sites = Sitecolumns.query.all()
    return sites

def add_images(title,url,description,userid):
    images = Images(title,url,description,datetime.datetime.now(),userid)
    db.session.add(images)
    db.session.commit()

def delete_images(imageId):
    current = Images.query.filter_by(id=imageId).first()
    if current is not None:
        db.session.delete(current)
        db.session.commit()

def update_images(imageId,title,url,description):
    current = Images.query.filter_by(id=imageId).first()
    if current is not None:
        current.title = title
        current.url = url
        current.description = description
        db.session.commit()

def get_images_all():
    images = Images.query.all()
    return images

def add_videos(title,fixurl,description,userid):
    videos = Videos(title,fixurl,description,datetime.datetime.now(),userid)
    db.session.add(videos)
    db.session.commit()

def delete_videos(videoId):
    current = videos.query.filter_by(id=videoId).first()
    if current is not None:
        db.session.delete(current)
        db.session.commit()

def update_videos(videoId,title,fixurl,description):
    current = Videos.query.filter_by(id=videoId).first()
    if current is not None:
        current.title = title
        current.fixurl = fixurl
        current.description = description
        db.session.commit()

def get_videos_all():
    videos = Videos.query.all()
    return videos