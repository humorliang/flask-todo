# coding:utf-8
import json
from app import create_app
from app.tools.my_exception import ApiException, HTTPException

app = create_app()




if __name__ == '__main__':
    app.run()
