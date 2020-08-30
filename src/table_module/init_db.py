from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.table_module.suit_table import SuitBase
from src.config.readconfig import config


def creat_db():
    # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    # 'mysql+mysqlconnector://root:user@ip:port/test'
    db_connect = 'mysql+' + config.get_dbinfo('mysql_connector') + '://' + config.get_dbinfo('username') + ':' + \
                 config.get_dbinfo('password') + '@' + config.get_dbinfo('host') + ':' + config.get_dbinfo('port') + \
                 '/' + config.get_dbinfo('db_name')
    return create_engine(db_connect)


db = sessionmaker(bind=creat_db())
session = db()


# 把类的数据类型映射到数据库
if __name__ == '__main__':
    engine = creat_db()
    SuitBase.metadata.create_all(engine)