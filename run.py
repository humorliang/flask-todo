# coding:utf-8
import json
from app import create_app
from app.tools.my_exception import ApiException, HTTPException

app = create_app()


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


if __name__ == '__main__':
    app.run()
