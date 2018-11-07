# coding:utf-8
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
from tools.my_exception import ApiException

# 定义蓝图 名称 位置 路径前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        info = {}
        # raise Exception('ee')
        # print(1/0)
        # if request.form:
        #     print(dict(request.form))
        #     username = request.form['username']
        #     password = request.form['password']
        #     info = {'status': 1, 'msg': 'success', 'data': request.form}
        # elif request.data:
        #     info = {'status': 1, 'msg': 'success', 'data': request.data}
        # else:
        #     info = {'status': 0, 'msg': 'error', 'data': '数据有误'}
        #     # 连接数据库
        # db = get_db()
        return json.dumps(info)
    else:
        return json.dumps({'msg': 0, 'data': '请使用post请求'})
