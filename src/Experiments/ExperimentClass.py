import src.LearningModelClasses.LearningModel as lm
import src.System.System as stm
from src.RewardClasses import RewardN as rm
import src.ModelClasses.Dancers as d
from dataclasses import dataclass
import numpy as np
import itertools
import copy
import os
import matplotlib.pyplot as plt


class Experiment:
    _system: stm.System
    _rewards: list[float]
    _dancers_init: list[stm.DancerInit]

    def __init__(self, dancers: list[stm.DancerInit], actions_dict: dict):
        self._dancers_init = copy.copy(dancers)
        self._system = stm.System(actions_dict, dancers)

    def run(self, iterations: int):
        rewards = []
        for i in range(iterations):
            iter_string = f"======================Iteration {i}======================\n"
            iter_string += f"START STATE: {self._system.state}\n"
            rewards.append(self._system.iteration())
            iter_string += f"Reward: {rewards[-1]}\n"
            iter_string += f"END STATE: {self._system.state}\n"
            print(iter_string)
        self._rewards = copy.deepcopy(rewards)

    @property
    def rewards(self):
        return copy.deepcopy(self._rewards)

    def save_results(self, path: str, name: str):
        os.mkdir(f"{path}/{name}")
        with open(f"{path}/{name}/data.txt", "x") as f:
            f.write(f"Experiment results: {name}\n\n")

            # Agent description
            f.write("1. Agents description.\n")
            for i, dancer in enumerate(self._dancers_init):
                f.write(f"\t1.{i}. Dancer\n")
                for line in str(dancer).split("\n"):
                    f.write("\t" + line + "\n")

            # System description
            f.write("\n2. System description.\n")
            f.write(f"\tIterations: {len(self._rewards)}\n")
            f.write(f"\tValence count: {len(self._system.actions)}\n")
            f.write(f"\tValences: {self._system.actions}\n")

            # Rewards data
            f.write("\n3. Rewards data.\n")
            f.write("\t" + str(self._rewards) + "\n")
            f.write("\n4. Rewards statistics.\n")
            less_0 = [r_i for r_i in self._rewards if r_i < 0]
            f.write("\t" + f"Less 0: {len(less_0)}" + "\n")
            greater_0 = [r_i for r_i in self._rewards if r_i >= 0]
            f.write("\t" + f"Greater or equal 0: {len(greater_0)}" + "\n")

        plt.plot(exp.rewards)
        plt.title(name)
        plt.xlabel("Iteration number")
        plt.ylabel("Total reward")
        plt.legend()
        plt.savefig(f"{path}/{name}/iteration_reward")


        """ less_0 = [r_i for r_i in self._rewards if r_i < 0]
        greater_0 = [r_i for r_i in self._rewards if r_i >= 0]
        print(len(less_0), len(greater_0))
        print(np.average(self._rewards))"""


if __name__ == "__main__":
    dancers = [
        stm.DancerInit(
            id=0,
            dancer=d.DancerData,
            dancer_params={"path": "../../dancer_data/data2/100.csv"},
            reward_model=rm.Reward,
            reward_model_params={},
            learning_model=lm.LearningModel,
            learning_model_params={"alpha": 0.2, "gamma": 0.5}
        ),
        stm.DancerInit(
            id=1,
            dancer=d.Dancer,
            dancer_params={},
            reward_model=rm.Reward,
            reward_model_params={"noise": True, "noise_type": "first_iterations", "noise_count": 20},
            learning_model=lm.LearningModel,
            learning_model_params={"alpha": 0.2, "gamma": 0.5}
        ),
        stm.DancerInit(
            id=2,
            dancer=d.Dancer,
            dancer_params={},
            reward_model=rm.Reward,
            reward_model_params={"noise": True, "noise_type": "first_iterations", "noise_count": 20},
            learning_model=lm.LearningModel,
            learning_model_params={"alpha": 0.2, "gamma": 0.5}
        ),

    ]

    actions_dict = {"Invite": False, "Dance": True}

    exp = Experiment(dancers, actions_dict)
    exp.run(5000)
    exp.save_results("../../ExperimentsResult", "test1")
