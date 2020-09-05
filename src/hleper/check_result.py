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
    :param keywords:[]
    :return:
    """
    if GlobalVar.get_response() is None or keywords is None:
        return body
    else:
        res = GlobalVar.get_response()
        for key in keywords:
            try:
                value = read_json_by_key(key, res)
                body = body.replace("$" + key, value)
            except Exception as e:
                print('参数替换错误：'+key)
        return json.dumps(body)


def check_result(response, expect):
    """
    检查结果
    :param response:请求结果 {}
    :param expect:预期结果 [()]
    :return:pass/fail
    """
    fail_time = 0
    for e in expect:
        try:
            check_type = e[0]
            check_key = e[1]
            check_value = e[2]
        except Exception as e1:
            print('预期结果解析错误：'+str(e))
        try:
            if check_type == 'equals' and check_value != read_json_by_key(check_key, response):
                fail_time += 1
            elif check_type == 'start-with' and not read_json_by_key(check_key, response).startswith(check_value):
                fail_time += 1
            elif check_type == 'end-with' and not read_json_by_key(check_key, response).endswith(check_value):
                fail_time += 1
            elif check_type == 'contain' and check_value not in read_json_by_key(check_key, response):
                fail_time += 1
        except Exception as e2:
            print('检查类型：'+check_type+'不存在')
    if fail_time != 0:
        return 'fail'
    else:
        return 'pass'


def read_json_by_key(key, res):
    if type(res) == 'str':
        res = json.loads(res)
    key = key.split('/')
    for k in key:
        if k.isdigit():
            k = int(k)
        res = res[k]
    return res