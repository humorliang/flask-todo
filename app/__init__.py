# coding:utf-8
import os

from flask import (Flask, g)


def create_app(test_config=None):
    '''flask工厂函数'''
    app = Flask(__name__, instance_relative_config=True)
    # app配置
    config_app(app, test_config)
    # 注册蓝图
    register_app(app)
    return app


def register_app(app):
    '''注册蓝图'''
    from . import auth, admin
    app.register_blueprint(auth.bp)  # 认证蓝图


def config_app(app, test_config=None):
    '''配置信息函数'''
    app.config.from_mapping(
        SECRET_KEY='sa!!id,}s*ha2@@#4',
    )
    # 附加配置信息
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
