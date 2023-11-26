

class ILearningModel:

    _alpha: float
    _gamma: float

    def __init__(self):
        raise NotImplementedError()

    @staticmethod
    def fit(model):
        raise NotImplementedError()