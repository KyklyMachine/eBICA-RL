from src.ModelClasses.IDancer import IDancer
from src.ModelClasses.Dancers import Dancer, People
from src.LearningModelClasses import LearningModel as lm
from src.RewardClasses import RewardN as rm
import copy
import itertools


class System:

    _states: dict[str: list[tuple]] = {}
    _state: dict[str: tuple] = {}
    _actions: dict[str: bool] = {}
    _dancers: dict[int: IDancer] = {}

    def __init__(self, actions: dict[str: bool], dancers: dict[int: type(IDancer)],
                 learning_modeles: list[lm.ILearningModel], reward_modeles: list[rm.IReward]):

        self._actions = actions

        for i, act in enumerate(actions.keys()):
            if actions[act]:
                dancers_to_product = []
                for k in range(len(dancers)):
                    lst = [i for i in range(len(dancers))]
                    lst.append(-1)
                    dancers_to_product.append(lst)
                self._states[act] = (
                    list(itertools.product(*dancers_to_product)))
            else:
                dancers_to_product = []
                for k in range(len(dancers)):
                    lst = [i for i in range(len(dancers)) if i != k]
                    lst.append(-1)
                    dancers_to_product.append(lst)
                self._states[act] = list(itertools.product(*dancers_to_product))

        for act in self._actions:
            self._state[act] = tuple([-1 for i in range(len(dancers))])

        for i in dancers:
            d = dancers[i](
                                    dancer_id=i,
                                    learning_model=learning_modeles[i],
                                    reward_model=reward_modeles[i],
                                    actions=self._actions,
                                    states=self._states,
                                    dancers=dancers,
                                    )
            q = copy.deepcopy(d._Q)
            d._Q = q
            self._dancers[i] = copy.copy(d)

    def set_state(self):
        state = {name: [] for name in self._actions.keys()}
        for i in range(len(self._dancers)):
            for state_val in state:
                state[state_val].append(self._dancers[i].action[state_val])
        for state_val in state:
            state[state_val] = tuple(state[state_val])
        self._state = state

    def iteration(self):
        print("START STATE:", self._state)
        for dancer in self._dancers.values():
            dancer.set_action(self._state)
        self.set_state()
        print("END STATE:", self._state)
        for dancer in self._dancers.values():
            dancer.update_q(self._state)


if __name__ == "__main__":

    actions_dict = {"Invite": False, "Dance": True}
    dancers_list = {0: Dancer, 1: Dancer, 2: Dancer}
    learning_modeles = [lm.LearningModel(), lm.LearningModel(), lm.LearningModel()]
    reward_modeles = [rm.Reward(), rm.Reward(), rm.Reward()]

    s = System(actions_dict, dancers_list, learning_modeles, reward_modeles)
    for i in range(100):
        print(f"======================Iteration {i}======================")
        s.iteration()
    #print(s._dancers[3]._Q["Invite"])





