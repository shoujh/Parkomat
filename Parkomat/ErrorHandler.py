class WrongNominalException(Exception):
    def __init__(self, info):
        super().__init__(info)


class InputFailure(Exception):
    def __init__(self, info):
        super().__init__(info)



