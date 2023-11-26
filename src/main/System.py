from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

import src.ModelClasses.Dancers as d
import src.LearningModelClasses.LearningModel as lm
from src.RewardClasses import RewardN as rm
import copy
import itertools


@dataclass
class DancerInit:
    id: int
    dancer: type(d.IDancer)
    learning_model: type(lm.ILearningModel)
    reward_model: type(rm.IReward)


class System:

    _states: dict[str: list[tuple]] = {}
    _state: dict[str: tuple] = {}
    _actions: dict[str: bool] = {}
    _dancers: dict[int: d.IDancer] = {}

    def __init__(self, actions: dict[str: bool], dancers: list[DancerInit]):

        self._actions = actions

        for i, act in enumerate(actions.keys()):
            if actions[act]:
                dancers_to_product = []
                for k in range(len(dancers)):
                    lst = [dancer.id for dancer in dancers]
                    lst.append(-1)
                    dancers_to_product.append(lst)
                self._states[act] = (
                    list(itertools.product(*dancers_to_product)))
            else:
                dancers_to_product = []
                for k in [dancer.id for dancer in dancers]:
                    lst = [dancer.id for dancer in dancers if dancer.id != k]
                    lst.append(-1)
                    dancers_to_product.append(lst)
                self._states[act] = list(itertools.product(*dancers_to_product))

        for act in self._actions:
            self._state[act] = tuple([-1 for i in range(len(dancers))])

        for i in range(len(dancers)):
            d = dancers[i].dancer(
                                    dancer_id=i,
                                    learning_model=dancers[i].learning_model(),
                                    reward_model=dancers[i].reward_model(),
                                    actions=self._actions,
                                    states=self._states,
                                    dancers=dancers,
                                    )
            q = copy.deepcopy(d._Q)
            d._Q = q
            self._dancers[i] = copy.copy(d)

    def set_state(self):
        """
        Update current state of the system (based on the current actions of the dancers)
        :return: None
        """
        state = {name: [] for name in self._actions.keys()}
        for i in range(len(self._dancers)):
            for state_val in state:
                state[state_val].append(self._dancers[i].action[state_val])
        for state_val in state:
            state[state_val] = tuple(state[state_val])
        self._state = state

    def iteration(self):
        """
        Performs a full cycle of updating the dancers' system:
            1) Dancers choose actions based on the most preferred
            2) The current state of the system is updated based on the selected actions of the dancers
            3) The weights in the matrix of states/actions (Matrix) are updated
        :return: The average reward for a given update cycle (based on selected actions and system updates)
        """
        for dancer in self._dancers.values():
            dancer.set_action(self._state)
        prev_state = copy.copy(self._state)
        self.set_state()
        rewards = []
        for dancer in self._dancers.values():
            rewards.append(dancer.update_q(self._state, prev_state))
        return np.sum(rewards)

    @property
    def state(self):
        """
        :return: Current system status
        """
        return self._state

    @property
    def actions(self):
        """
        :return: All possible of dancers
        """
        return self._actions

    @property
    def states(self):
        """
        :return: All possible states of the dancers' system for each valence
        """
        return self._states


if __name__ == "__main__":

    dancers = [
        DancerInit(
            id=0,
            dancer=d.Dancer,
            learning_model=lm.LearningModel,
            reward_model=rm.Reward
                   ),
        DancerInit(
            id=1,
            dancer=d.Dancer,
            learning_model=lm.LearningModel,
            reward_model=rm.Reward
        ),
        DancerInit(
            id=2,
            dancer=d.Dancer,
            learning_model=lm.LearningModel,
            reward_model=rm.Reward
        ),
    ]

    actions_dict = {"Invite": False, "Dance": True}

    s = System(actions_dict, dancers)
    r = []
    for i in range(500):
        print(f"======================Iteration {i}======================")
        #print("START STATE:", s.state)
        r.append(s.iteration())

        #print("END STATE:", s.state)
    """
    plt.plot(r)
    plt.show()
    """






