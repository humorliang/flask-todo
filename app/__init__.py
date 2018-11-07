# coding:utf-8
import os
import werkzeug
import json
from config import config
from flask import (Flask, g)

from tools.my_exception import ApiException, HTTPException


def create_app(test_config=config):
    '''flask工厂函数'''
    app = Flask(__name__, instance_relative_config=True)
    # app配置
    config_app(app, test_config)
    # 注册蓝图
    register_app(app)

    error_handler(app)
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


def error_handler(app):
    '''创建'''

    # 注册全局异常错误
    @app.errorhandler(Exception)
    def error_500(e):
        # api 异常
        if isinstance(e, ApiException):
            app.logger.exception('error 500: %s', e)
            print('api except')
            return e
        # http异常
        elif isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            error_code = 10001
            print('http except')
            app.logger.exception('error 500: %s', e)
            return ApiException(code=code, msg=msg, error_code=error_code)
        # Exception异常
        elif isinstance(e, Exception):
            code = '500'
            msg = e.__repr__()
            error_code = 10002
            print('exception')
            return ApiException(code=code, msg=msg, error_code=error_code)
        else:
            if not app.config['DEBUG']:
                app.logger.exception('error 500: %s', e)
                return ApiException()
            raise e
