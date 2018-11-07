# coding:utf-8
import requests
# from app.tools.api_exceptions import api_except
import base64


# @api_except
def get(url):
    res = requests.get(url)
    print(res.json())


# @api_except
def post(url, data):
    res = requests.post(url, data=data)
    print(res.text)


s = 'abcde'
# 被编码的字符串必须为字节类型
bs = base64.b64encode(s.encode('utf-8'))
# bs = base64.b64encode(s)
print(bs)

# if __name__ == '__main__':
#     register_url = 'http://127.0.0.1:5000/auth/register'
#     # get(register_url)
#     _dict = {'username': '17312349876'}
#     # post(register_url, _dict)
