from src.ModelClasses.IDancer import IDancer
from src.RewardClasses.IReward import IReward
from src.LearningModelClasses.ILearningModel import ILearningModel
import numpy as np


class Dancer(IDancer):

    def __init__(self,
                 learning_model: ILearningModel,
                 reward_model: IReward,
                 actions: list[list[str]],
                 states: list[list[str]]):
        self._learning_model = learning_model
        self._reward_model = reward_model
        self._actions = actions
        self._states = states

    def __str__(self):
        return "Dancer(IDancer)"

    def set_action(self, state):
        pass

    def get_action(self):
        raise NotImplementedError()

    def update_q(self):
        pass


class People(IDancer):

    def __init__(self,
                 actions: list[list[str]],
                 states: list[list[str]],
                 learning_model: ILearningModel=None,
                 reward_model: IReward=None
                 ):
        self._actions = actions
        self._states = states
        pass

    def __str__(self):
        return "People(IDancer)"

    def set_action(self, state: list[str]):
        act_strings = []
        for i, acts in enumerate(self._actions):
            act_string = "Введите номер действия:\n"
            for j, act in enumerate(acts):
                act_string += f"{j} – {act}\n"
            act_string += "Ввод: "
            act_number = int(input(act_string))
            act_string = acts[act_number]
            if act_number not in np.arange(len(acts)):
                print("Неверный номер действия! Повторите ввод.")
                return self.commit_act(state)
            act_strings.append(act_string)

        self._action = act_strings

    def get_action(self):
        return self._action

    def update_q(self):
        pass


if __name__ == "__main__":

    Actions = [["11", "12"], ["21", "22"]]
    States = [["11", "12"], ["21", "22"]]

    p = People(Actions, States)
    print(str(p))
    p.set_action(["11", "22"])