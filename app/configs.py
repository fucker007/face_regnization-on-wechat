#_*_ coding: utf-8 _*_
import os

root_path = os.path.dirname(__file__)
#公共信息配置位置
configs = dict(
    static_path = os.path.join(root_path,"static"),
    debug = True #开启调试模式

)

mongodb_configs = dict(
    db_host = '106.14.200.68',
    db_port = 27017
)