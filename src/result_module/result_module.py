import json

from src.hleper import check_result


class ResultModule:

    def __init__(self):
        self.id = None
        self.url = ''
        self.api_name = ''
        self.case_name = ''
        self.request_method = ''
        self.request_body = ''
        self.expect_result = ''
        self.response_data = ''
        self.key_words = []
        self.result = ''
        self.test_time = ''

    @property
    def to_html_json(self):
        _res = self.__dict__
        _res.pop('url')
        _res.pop('test_time')
        _res.pop('key_words')
        return json.dumps(_res)

    @property
    def to_excel_list(self):
        _res = []
        for key, value in self.__dict__.items():
            if key != 'key_words':
                _res.append(value)
        return _res

    @property
    def expect(self):
        # 返回一个元祖list
        return check_result.cut_expect_result(self.expect_result)