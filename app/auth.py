# coding:utf-8
import json

import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

# 定义蓝图 名称 位置 路径前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        info = {}

        info = {"success": True, 'data': ''}
        return json.dumps(info)
    else:
        return json.dumps({'msg': 0, 'data': '请使用post请求'})
