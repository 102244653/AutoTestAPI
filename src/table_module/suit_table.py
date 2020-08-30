from datetime import datetime
from sqlalchemy import Column, String, Integer, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

from src.table_module.base import Base

SuitBase = declarative_base()


class SuitModule(SuitBase, Base):
    __tablename__ = 'suit_case'
    id = Column(Integer, autoincrement=True, primary_key=True)  # id
    case_table = Column(String(10), nullable=False)
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
