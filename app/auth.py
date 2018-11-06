# coding:utf-8
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db  # 导入数据库

# 定义蓝图 名称 位置 路径前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')
