class ModelBuilerMock:
    def __init__(self):
        pass

    def build(self, params):
        mul = 1
        for param in params:
            val = params[param]
            mul = mul*val
        return mul


