# coding:utf-8
import re

from pymysql import DataError
from config import config
from flask import (Flask, request, abort)
from tools.my_exception import (ApiException, HTTPException)


def create_app(test_config=config):
    '''flask工厂函数'''
    app = Flask(__name__, instance_relative_config=True)
    # app配置
    config_app(app, test_config)
    # 注册蓝图
    register_app(app)
    # 异常错误处理
    error_handler(app)
    # 请求数据统一处理
    request_handler(app)
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
    '''创建处理错误异常'''

    # 注册全局异常错误
    @app.errorhandler(Exception)
    def error_or_except(e):
        # api 异常
        if isinstance(e, ApiException):
            print('api except')
            return e
        # http异常
        elif isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            print('http except')
            return ApiException(code=code, msg=msg)
        # Exception异常
        elif isinstance(e, Exception):
            if isinstance(e, DataError):
                code = 500
                # 将异常的信息传递给msg
                msg = e.__repr__()
                print('db exception')
                return ApiException(code=code, msg=msg)
            else:
                code = 500
                # 将异常的信息传递给msg
                msg = e.__repr__()
                print('exception')
                return ApiException(code=code, msg=msg)
        else:
            if not app.config['DEBUG']:
                print('debug')
                return ApiException()
            raise e


def request_handler(app):
    '''请求信息处理句柄'''

    @app.before_request
    def request_data_type():
        '''返回统一的数据格式
        :return dict类型参数
        '''
        if request.method == 'POST':
            request._dict = {}
            if request.form:
                for key, value in dict(request.form).items():
                    # re.sub('正则'，'替换符'，被匹配字符)  XML 乱码 过滤 post
                    request._dict[key] = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", "", str(value[0]))
                print(request._dict)
            elif request.get_json():
                # print('json', request.get_json())
                request._dict = dict(request.get_json())
            elif request.values:
                # print('values', request.values)
                request._dict = dict(request.values)
            else:
                abort(400, {'success': False, 'data': '请求有误！请求的数据为form或json类型数据不能为空！'})
        else:
            pass

    @app.before_request
    def ip_filter():
        '''过滤IP地址'''
        # IP = request.remote_addr
        # print(IP) # 获取客户端的IP，需要设置web服务器不然就只是127.0.0.1
        pass
