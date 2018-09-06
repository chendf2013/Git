import logging
import pymysql

from flask_script import Manager
from flask import session
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db, models

# 类似于工厂方法
app = create_app('development')
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    # print(app.url_map)
    manager.run()