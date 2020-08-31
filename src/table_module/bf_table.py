# 业务流模块
import json
from datetime import datetime
from src.table_module.base import Base
from sqlalchemy import Column, String, SmallInteger, Integer
from sqlalchemy.ext.declarative import declarative_base

BfBase = declarative_base()


class BfModule(BfBase, Base):
    __tablename__ = 'bf_case'
    id = Column(Integer, autoincrement=True, primary_key=True)  # id
    bf_name = Column(String(10), nullable=False)  # 业务流名称
    api_name = Column(String(10), nullable=False)  # 接口名称
    case_name = Column(String(20), nullable=False, unique=True)  # 用例名
    request_method = Column(String(6), nullable=False)  # 请求方式
    request_body = Column(String(250), nullable=False)  # 请求内容
    expect_result = Column(String(100), nullable=False)  # 预期结果
    key_words = Column(String(100))  # 传递给下一个接口的参数   [data/1/username,password,token/2]
    status = Column(SmallInteger, default=1)  # 状态：1-有效 ，0-无效
    update_time = Column(Integer)  # 更新时间

    def __init__(self):
        self.update_time = int(datetime.now().timestamp())

    @property
    def read_update_time(self):
        # 格式化时间
        if self.update_time:
            return datetime.fromtimestamp(self.update_time)
        else:
            return None

    @property
    def to_body(self):
        return str(self.request_body)





