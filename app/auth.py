# coding:utf-8
import json
from flask import (
    Blueprint, request, session, url_for,
    redirect)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import (get_db, close_db, str_escape)

# 定义蓝图 名称 位置 路径前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        info = {}
        data = request._dict
        if data.get('username') and data.get('password'):
            # print(type(data.get('password')))  type
            username = data.get('username')
            password = data.get('password')
            db = get_db()
            try:
                with db.cursor() as cur:
                    record_num = cur.execute("SELECT * FROM user WHERE username=%s", (username,))
                    if record_num == 0:
                        cur.execute("INSERT INTO user(username,password) VALUES (%s,%s)",
                                    (username, generate_password_hash(password)))
                        db.commit()
                        info = {"success": True, 'data': '注册成功'}
                    else:
                        info = {"success": False, "data": '用户名已存在！'}
            finally:
                close_db()
        else:
            info = {"success": False, "data": '用户名和密码不能为空！'}
        return json.dumps(info)
    else:
        return json.dumps({'success': False, 'data': '请使用post请求'})


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request._dict
        info = {}
        username = data.get('username')
        password = data.get('password')  # 元组
        db = get_db()
        if username and password:
            try:
                with db.cursor() as cur:
                    cur.execute("SELECT id,username,password FROM user WHERE username=%s", (username,))
                    user = cur.fetchone()
                    print(user)
                    if user is None:
                        info = {"success": False, "data": "用户名不存在"}
                        return json.dumps(info)
                    else:
                        if check_password_hash(user[2], password):
                            info = {"success": True, "data": {"id": user[0], "username": user[1]}}
                            session.clear()
                            session['user_id'] = user[0]
                            return json.dumps(info)
                        else:
                            info = {"success": False, "data": "密码错误！"}
                            return json.dumps(info)
            finally:
                db.close()
    else:
        return json.dumps({'success': False, 'data': '请使用post请求'})


@bp.route('/login_out', methods=['GET', 'POST'])
def login_out():
    session.clear()
    return json.dumps({"success":True,"data":'注销成功'})
