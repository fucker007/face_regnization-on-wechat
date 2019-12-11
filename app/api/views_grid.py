# _*_ coding: utf-8 _*_
import tornado.gen
import tornado.concurrent
from app.api.view_common import CommonHandler
class GridHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        grids = {
            'style':'width:50%',
            'logo' : self.site_url + '/static/images/title.jfif',
            'name' : '快捷导航',
            'data' :[
                {
                    'name':'人脸检测',
                    'image':self.site_url + '/static/images/face_0.png',
                    'url':'/pages/match/match?cate=1&uuid='
                },
                {
                    'name': '人脸勾勒',
                    'image': self.site_url + '/static/images/face_1.png',
                    'url': '/pages/match/match?cate=2&uuid='
                },
                {
                    'name': '人脸美化',
                    'image': self.site_url + '/static/images/face_2.png',
                    'url': '/pages/match/match?cate=3&uuid='
                },
                {
                    'name': '人脸化妆',
                    'image': self.site_url + '/static/images/face_3.png',
                    'url': '/pages/match/match?cate=4&uuid='
                },
                {
                    'name': '人脸搞怪',
                    'image': self.site_url + '/static/images/face_4.png',
                    'url': '/pages/match/match?cate=5&uuid='
                },
                {
                    'name': '关于',
                    'image': self.site_url + '/static/images/face_5.png',
                    'url': '/pages/about/about'
                },
            ]
        }
        self.write(grids)