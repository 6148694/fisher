from  flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")  # 载入配置文件
    app.config.from_object("app.setting")  # 载入配置文件
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

