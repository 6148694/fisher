#coding:utf-8
from urllib import parse
pwd_encoded = parse.quote_plus("Gaojunqing111@")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{pwd_encoded}@39.107.60.13:3306/fishers?charset=utf8"
