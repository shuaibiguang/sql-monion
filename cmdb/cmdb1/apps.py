from django.apps import AppConfig


class Cmdb1Config(AppConfig):
    name = 'cmdb1'

#     数据库部分
    db_engine = "django.db.backends.mysql"
    db_name = "cmdb"
    db_user = "root"
    db_password = ""
    db_host = "127.0.0.1"
    db_port = "3306"
