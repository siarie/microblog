import os

basepath = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'write-your-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basepath, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_LTS = os.environ.get('MAIL_USE_LTS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    ADMINS = ['sriaspari@gmail.com']