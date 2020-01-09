from flask import Blueprint
from flask import request

search_blue = Blueprint('search', __name__)


@search_blue.route('/')
def search():
    method = request.method
    # 判断请求方式
    if method == 'GET':
        print('请求是GET，请求成功!')
        return '返回搜索结果'
    else:
        print('请求方式不是GET,只支持GET请求')
        return '请求方式不正确拒绝访问'
