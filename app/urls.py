# _*_ coding: utf-8 _*_
from app.admin.view_index import IndexHandler as admin_index
from app.api.view_index import IndexHandler as api_index
from app.api.views_user import UserHandler as api_user
from app.api.views_grid import GridHandler as api_grids
from app.api.views_match import MatchHandler as api_match
#这里是路由文件


#API接口
api_urls = [
    (r'/',api_index),
    (r'/user/',api_user),
    (r'/grids/',api_grids),
    (r'/match/',api_match),
]

#后台系统
admin_urls = [
    (r'/',admin_index)
]

#urls汇总
urls = api_urls + admin_urls
# urls = api_urls
print(urls)