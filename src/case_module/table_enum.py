from enum import Enum

from src.case_module.bf_table import BfModule
from src.case_module.init_db import session


class Table(Enum):
    bf = session.query(BfModule)