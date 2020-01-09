from app.main import app
from app.search.view import search_blue


# 对app进行蓝图注册
app.register_blueprint(search_blue, url_prefix='/search')
