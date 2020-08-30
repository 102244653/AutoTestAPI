class GlobalVar:

    Token = ''
    Session = ''
    AllCase = []
    FPCase = []
    BFCase = []
    FailCase = []
    PassCase = []
    SkipCase = []
    ReadFailCase = []
    Response = None

    @staticmethod
    def set_token(token):
        GlobalVar.Token = token

    @staticmethod
    def get_token():
        return GlobalVar.Token

    @staticmethod
    def set_session(session):
        GlobalVar.Session = session

    @staticmethod
    def get_session():
        return GlobalVar.Session

    @staticmethod
    def set_allcase(allcase):
        GlobalVar.AllCase.append(allcase)

    @staticmethod
    def get_allcase():
        return  GlobalVar.AllCase

    @staticmethod
    def set_bfcase(bfcase):
        GlobalVar.BFCase.append(bfcase)

    @staticmethod
    def get_bfcase():
        return GlobalVar.BFCase

    @staticmethod
    def set_fpcase(fpcase):
        GlobalVar.FPCase.append(fpcase)

    @staticmethod
    def get_fpcase():
        return GlobalVar.FPCase

    @staticmethod
    def set_passcase(passcase):
        GlobalVar.PassCase.append(passcase)

    @staticmethod
    def get_passcase():
        return GlobalVar.PassCase

    @staticmethod
    def set_failcase(failcase):
        GlobalVar.FailCase.append(failcase)

    @staticmethod
    def get_failcase():
        return GlobalVar.FailCase

    @staticmethod
    def set_skipcase(skipcase):
        GlobalVar.SkipCase.append(skipcase)

    @staticmethod
    def get_skipcase():
        return GlobalVar.SkipCase

    @staticmethod
    def set_readfailcase(case):
        GlobalVar.ReadFailCase.append(case)

    @staticmethod
    def get_readfailcase():
        return GlobalVar.ReadFailCase

    @staticmethod
    def set_response(response):
        GlobalVar.Response = response

    @staticmethod
    def get_response():
        return GlobalVar.Response

    @staticmethod
    def delete_response():
        GlobalVar.response = None