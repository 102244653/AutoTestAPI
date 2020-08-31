from src.result_module.result_module import ResultModule
from src.config.readconfig import config
from src.hleper.check_result import replace_param_in_json, check_result
from src.hleper.tool import read_local_time
from src.http.http_request import *
from src.table_module.table_enum import query
from src.config.globalvar import GlobalVar


def read_suit_case():
    """
    读取suit_case表里面需要执行测试的表名
    :return: []
    """
    suit = []
    for s in query('suit_case'):
        suit.append(s.case_table)
    if len(suit) == 0:
        print("#####################################################################")
        print("###########################暂无可执行用例############################")
        print("#####################################################################")
        return
    else:
        return suit


def read_case_by_table(evn, table_name):
    case_list = []
    all_case = query(table_name)
    if all_case:
        for case in all_case:
            new_case = ResultModule()
            try:
                new_case.id = case.id
                new_case.api_name = case.api_name
                new_case.url = config.get_host(evn) + config.get_uri(case.api_name)
                new_case.case_name = case.case_name
                new_case.request_method = case.request_method
                new_case.expect_result = case.expect_result
                new_case.request_body = case.request_body
                if table_name == 'bf_case' and case.key_words is not None:
                    new_case.key_words = eval(case.key_words)
                else:
                    new_case.key_words = []
            except Exception as e:
                GlobalVar.set_readfailcase(case.case_name)
                print("*******************" + table_name+'::'+case.case_name+ "表用例读取失败*******************")
                print(e)
            case_list.append(new_case)
    return table_name, case_list


def execute_case(table_name, case_list):
    for case in case_list:
        if table_name == 'bf_case':
            GlobalVar.set_bfcase(case.case_name)
        else:
            GlobalVar.set_fpcase(case.case_name)
        try:
            if table_name == 'bf_case' and '$' in case.request_body:
                case.request_body = replace_param_in_json(case.request_body, case.key_words)
                GlobalVar.delete_response()
            if case.request_method == 'get':
                code, case.response_data = auto_get(case.url+case.request_body)
            if case.request_method == 'post':
                code, case.response_data = auto_post(case.url, case.request_body)
        except Exception as e:
            case.response_data = '{"result": "error"}'
        finally:
            GlobalVar.set_response(case.response_data)
            case.result = check_result(case.response_data, case.expect)
            case.test_time = read_local_time()
            if case.result == 'pass':
                GlobalVar.set_passcase(case.case_name)
            else:
                GlobalVar.set_failcase(case.case_name)
        GlobalVar.set_allcase(case)
