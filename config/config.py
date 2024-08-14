class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost/train06'
    SECRET_KEY = 'your_strong_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    JWT_TOKEN_LOCATION = ['headers']
