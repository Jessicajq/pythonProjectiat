#-*-coding:utf-8-*-
from flask import Flask,blueprints
from datetime import timedelta
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['UPLOAD_FILE_FOLDER'] = 'static/proxy/uploads/'
app.config['UPLOAD_TEST_FILE_FOLDER'] = 'static/file/uploads/'
app.config['DOMAIN'] = 'http://127.0.0.1:5001/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif','HTML','html','xlsx'])
app.config['SECRET_KEY']= "thisisaverycooltestpalt" #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=1) #设置session的保存时间。

'''
数据库对象创建
'''
from flask_sqlalchemy import SQLAlchemy

#我本地 app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost:3306/ITA?charset=utf8mb4"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ailpha123456@10.50.2.202:33306/IAT?charset=utf8mb4"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_POOL_SIZE"] = 100
app.config["SQLALCHEMY_POOL_RECYCLE"] = 8
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
db.metadata.clear()
socketio = SocketIO(app, cors_allowed_origins='*')

'''
注册蓝图
'''
from .build.login import auth
app.register_blueprint(auth, url_prefix='/api/auth')

from .build.user import user
app.register_blueprint(user, url_prefix='/api')

from .IAT.api import api
app.register_blueprint(api, url_prefix='/api/IAT')

from .IAT.case import iatCase
app.register_blueprint(iatCase, url_prefix='/api/IAT/case')

from .IAT.wstask import wstask
app.register_blueprint(wstask)