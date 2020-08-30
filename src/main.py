from src.case_module.table_enum import Table

if __name__ == '__main__':

    bf = Table.bf.value.all()
    print(len(bf))
    # for i in bf:
    #     print(str(i.double_to_dict()))
    a = bf[0]
    print(str(a.id))