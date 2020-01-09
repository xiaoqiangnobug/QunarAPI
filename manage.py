# 项目启动文件
from app.main.views import app

if __name__ == '__main__':
    app.run(threaded=True)