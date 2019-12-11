import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    #定义一个GET请求方法
    def get(self,*args,**kwargs):
        self.write("<h1 style='color:green'> 这是后台管理系统</h1>")