import json
from datetime import datetime

from src.table_module.base import Base
from src.config.readconfig import config
from src.hleper import check_result
from sqlalchemy import Column, String, Integer, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

LoginBase = declarative_base()


class LoginModule(LoginBase, Base):
    __tablename__ = 'login_case'
    id = Column(Integer, autoincrement=True, primary_key=True)  # id
    api_name = Column(String(10), nullable=False)  # 接口名称
    case_name = Column(String(20), nullable=False, unique=True)  # 用例名
    request_method = Column(String(6), nullable=False)  # 请求方式

    # 请求字段
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

    expect_result = Column(String(100), nullable=False)  # 预期结果
    status = Column(SmallInteger, default=1)  # 状态：1-有效 ，0-无效
    update_time = Column(Integer)  # 更新时间

    @property
    def uri(self):
        if self.api_name:
            return config.get_uri(self.api_name)
        else:
            return ''

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
        return {"username": self.username, "password1": self.password}