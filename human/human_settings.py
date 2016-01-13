import os

BLOG_TITLE = 'Humans in Urumuqi'
SECRET_KEY = 'u%23#ru$mu(qi*)'

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/human.db' % os.path.dirname(__file__)
SQLALCHEMY_ECHO = False
DEBUG = True
PORT = 5000