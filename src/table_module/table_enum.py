from src.table_module.bf_table import BfModule
from src.table_module.init_db import session
from src.table_module.login_table import LoginModule
from src.table_module.suit_table import SuitModule


class TableDict:
    table = {
        'suit_case': SuitModule,
        'bf_case': BfModule,
        'login_case': LoginModule
    }


def query(name):
    if name in TableDict.table.__dict__:
        table = TableDict.table[name]
        return session.query(table).filter(table.status == 1).order_by(table.id).all()
    else:
        return None


# def query_bf_name():
#     bf = session.query(BfModule).filter(BfModule.status == 1).order_by(BfModule.id).group_by(BfModule.bf_name).all()
#     return bf.double_to_dict