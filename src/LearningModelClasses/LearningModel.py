from src.LearningModelClasses.ILearningModel import ILearningModel
from src.ModelClasses.IDancer import IDancer


class LearningModel(ILearningModel):

    s_prev: float

    def __init__(self):
        super().__init__()

    @staticmethod
    def fit(model: IDancer):
        pass