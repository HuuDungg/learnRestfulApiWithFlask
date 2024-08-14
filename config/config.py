from datetime import timedelta
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost/train06'
    SECRET_KEY = 'TranHuuDung'
    JWT_SECRET_KEY = 'Tran HuuTung'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)