from src.Containers import QMatrix
from src.RewardClasses.IReward import IReward
from src.LearningModelClasses.ILearningModel import ILearningModel


class IDancer:

    _reward_model: IReward
    _Q: list[QMatrix]

    _learning_model: ILearningModel

    _actions: list[list[str]]
    _action: list[str]

    _states: list[list[str]]

    def __init__(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    def set_action(self, state):
        raise NotImplementedError()

    def get_action(self):
        raise NotImplementedError()

    def update_q(self):
        raise NotImplementedError()

