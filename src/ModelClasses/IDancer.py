from src.Containers import QMatrix
from src.RewardClasses.IReward import IReward
from src.LearningModelClasses.ILearningModel import ILearningModel


class IDancer:

    _reward_model: IReward
    _Q: dict[str: QMatrix] = {}

    _learning_model: ILearningModel

    _actions: dict[str: bool]
    _action: dict[any]

    _states: dict[str: list[str]]

    _id: any

    _dancers: dict

    def __str__(self):
        raise NotImplementedError()

    def set_action(self, state: dict[str: tuple]):
        raise NotImplementedError()

    def get_action(self):
        raise NotImplementedError()

    def update_q(self, state: dict[str: tuple], prev_state: dict[str: tuple]):
        raise NotImplementedError()

