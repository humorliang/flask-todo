# coding:utf-8
from flask import request, json
from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    '''
    请求异常基类，
    code: 服务器错误状态码
    msg : 错误内容
    error：错误编码
    '''
    code = 500
    msg = '未知错误'
    error_code = 50001

    def __init__(self, code=None, msg=None, error_code=None, header=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        # 继承HttpException然后再重构 HttpException 构造函数参数：description=None, response=None
        super().__init__(msg, None)

    # 重写父类get_body方法 返回特定的body 信息
    def get_body(self, environ=None):
        """Get the HTML body."""
        body = {
            'success': False,
            'data': {
                'code': self.code,
                'error_code': self.error_code,
                'msg': self.msg,
                'path': request.full_path,
                'description': super().get_description(environ)
            }
        }
        return json.dumps(body)

    # 重写父类的get_headers方法 返回特定的头信息
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]
