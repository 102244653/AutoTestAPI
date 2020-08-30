# 业务流模块
from datetime import datetime

from src.case_module.base import Base
from src.config.readconfig import config
from src.hleper import check_result
from sqlalchemy import Column, String, SmallInteger, Integer
from sqlalchemy.ext.declarative import declarative_base

BfBase = declarative_base()


class BfModule(BfBase, Base):
    __tablename__ = 'bf_case'
    id = Column(Integer, autoincrement=True, primary_key=True)  # id
    case_type = Column(String(2), nullable=False, default='bf')  # 用例类型：bf-业务流，fp-功能点
    bf_name = Column(String(10), nullable=False)  # 业务流名称
    api_name = Column(String(10), nullable=False)  # 接口名称
    case_name = Column(String(20), nullable=False, unique=True)  # 用例名
    request_method = Column(String(6), nullable=False)  # 请求方式
    request_body = Column(String(250), nullable=False)  # 请求内容
    expect_result = Column(String(100), nullable=False)  # 预期结果
    status = Column(SmallInteger, default=1)  # 状态：1-有效 ，0-无效
    update_time = Column(Integer)  # 更新时间

    @property
    def uri(self):
        if self.api_name:
            return config.get_uri(self.api_name)
        else:
            return ''

    @property
    def expect(self):
        # 返回一个元祖list
        return check_result.cut_expect_result(self.expect_result)

    def __init__(self):
        self.update_time = int(datetime.now().timestamp())

    @property
    def read_update_time(self):
        # 格式化时间
        if self.update_time:
            return datetime.fromtimestamp(self.update_time)
        else:
            return None




