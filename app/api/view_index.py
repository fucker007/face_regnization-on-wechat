import time
import tornado.gen
import tornado.concurrent
from app.api.view_common import CommonHandler
class IndexHandler(CommonHandler):
    #定义一个GET请求方法

    @tornado.gen.coroutine
    def get(self,*args,**kwargs):
        yield self.get_response()

    #让阻塞的代码在线程池中运行
    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.write(self.common_params) #字典默认转化为json响应
        # time.sleep(6)
        # self.write("<h1 style='color:green'>这是API接口</h1>")
        # self.write("<h1 style='color:red'>数据库信息: {}</h1>".format(
        #     str(self.md)
        # ))
