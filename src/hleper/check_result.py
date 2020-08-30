import json

from src.config.globalvar import GlobalVar


def cut_expect_result(expect_result):
    # 格式  equals[success:1];contain[lists:中国,广东,中山]
    """
    分割预期结果
    :param expect_result:
    :return: [()]
    """
    expect = []
    if expect_result is not None:
        res = expect_result.strip().split(';')
        for r in res:
            _check = ()
            _res = r.split('[')
            _check[0] = _res[0].strip()
            _check[1] = _res[1].replace(']', '').split(':')[0]
            _check[2] = _res[1].replace(']', '').split(':')[1]
            expect.append(_check)
    return expect


def replace_param_in_json(body, keywords):
    """
    替换json里面的参数化字段
    :param body:
    :param param:
    :return:
    """
    if GlobalVar.get_response() is None or keywords is None:
        return body
    else:
        res = GlobalVar.get_response()
        _var = dict()
        for key in keywords:
            _var[key] = read_json_by_key(key, res)
        for key, value in _var.items():
            body = body.replace("$"+key, value)
        return json.dumps(body)


def check_result(response, expect):
    """
    检查结果
    :param response:请求结果 {}
    :param expect:预期结果 [()]
    :return:pass/fail
    """
    result = ''



def read_json_by_key(key, json):
    return ''