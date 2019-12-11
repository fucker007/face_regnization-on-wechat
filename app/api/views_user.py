# _*_ conding:uf-8 _*_

from app.api.view_common import CommonHandler
import tornado.gen
import tornado.concurrent
#定义用户登录视图
class UserHandler(CommonHandler):
    #跨域访问

    def check_xsrf_cookie(self):
        return True

    #post请求
    @tornado.gen.coroutine
    def post(self,*args, **kwargs):
        yield self.post_response()

    # 耗时处理
    @tornado.concurrent.run_on_executor
    def post_response(self):
        result = dict(
            code=0,
            msg='失败',

        )
        #添加数据进行组装,**展开字符进行组装
        data = dict(
            self.params,
            **self.common_params
        )
        #插入到数据库
        db = self.md.model_project
        #把数据插入到集合中
        record = db.loginlog.insert_one(data)
        last_id = record.inserted_id
        if last_id:
            result = dict(
                code = 1,
                msg = '成功',
                last_id = str(last_id),

            )
        #响应接口
        self.write(result)

