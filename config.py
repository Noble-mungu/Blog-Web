import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://wdcxvpbiuqzqkt:b30015b65c62dd26626b3608efee15cb1f3337a16cb3731c079bf9c5f7a3e55e@ec2-54-165-164-38.compute-1.amazonaws.com:5432/d6rop9esgvakft'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='wertyuiokjhvxcvbn'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DEBUG = True