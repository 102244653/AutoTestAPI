import configparser
import json
import os
import base_path


class ReadConfig(object):

    def __init__(self, path=None):
        if path:
            config_path = path
        else:
            root_dir = base_path.get_path()
            config_path = os.path.join(root_dir, 'src/config/config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_dbinfo(self, param):
        """
        读取数据库信息
        :param param:
        :return:
        """
        return self.cf.get('database', param)

    def get_uri(self, param):
        """
        读取接口uri
        :param param:
        :return:
        """
        uri = ''
        try:
            uri = self.cf.get('api-uri', param)
        except Exception as e:
            raise Exception('not found api-uri in config[api-uri]')
        finally:
            return uri

    def get_host(self, param):
        return self.cf.get('evn', param)

    # def read_json(self, param):
    #     """
    #     读取json文件
    #     :return:
    #     """
    #     path = '{}/src/config/helplist.json'.format(base_path.get_path())
    #     with open(path, 'r') as load_f:
    #         load_dict = json.load(load_f)
    #     return load_dict[param]['titles']


config = ReadConfig()

if __name__ == '__main__':
    print(config.get_dbinfo('port'))

