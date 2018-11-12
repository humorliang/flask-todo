# coding:utf-8
import pymysql
from flask import current_app, g


# 获取数据库对象
def get_db():
    if 'db' not in g:
        # host user password database port chartset
        g.db = pymysql.connect(
            host=current_app.config['HOST'],
            user=current_app.config['USER_NAME'],
            port=3306,
            password=current_app.config['PASSWORD'],
            database=current_app.config['DATABASE_NAME'],
            charset='utf8'
        )
    return g.db


# 关闭数据库连接
def close_db():
    # 数据库对象
    db = g.pop('db', None)
    if db is not None:
        db.close()


# 处理字符串转义
def str_escape(_str):
    return pymysql.escape_string(_str)


if __name__ == '__main__':
    print(str_escape('adsd'))
