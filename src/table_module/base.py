
class Base:
    # 讲对象装转换成dict
    @property
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def double_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    @property
    def to_list(self):
        _res = []
        for x in self.__dict__.values():
            _res.append(x)
        return _res







