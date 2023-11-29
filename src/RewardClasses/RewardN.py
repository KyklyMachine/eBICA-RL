import copy
import random

from src.RewardClasses.IReward import IReward


class StateHistory:
    _data: list
    _max_history_size: int

    def __init__(self, max_history_size=20):
        self._data = []
        self._max_history_size = max_history_size

    def __len__(self):
        return len(self._data)

    def append(self, data_item):
        self._data.append(data_item)
        if len(self._data) > self._max_history_size:
            self._data.pop(0)

    @property
    def data(self):
        return copy.deepcopy(self._data)

    def __getitem__(self, item):
        if len(self._data) - 1 < item:
            raise IndexError(f"Index out of range. Last index of the data is {len(self._data) - 1}"
                             f", requested index is {item}.")
        """if item < 0:
            raise IndexError(f"Index out of range. First index of the data is {0 if self._data else None}"
                             f", requested index is {item}.")"""
        return copy.deepcopy(self._data[item])


class Reward(IReward):
    """
    Description of Reward
    """

    _is_noise: bool
    _noise_type: str
    _noise_count: int
    _iteration: int = 0

    _history: StateHistory

    def __init__(self, noise=True, noise_type="first_iterations", noise_count=0):
        self._is_noise = noise
        self._noise_type = noise_type
        self._noise_count = noise_count
        self._history = StateHistory()

    def reward(self, state, action, dancer_id):

        total_reward = 0

        # Inviting a partner
        if action["Invite"] != -1:
            total_reward += 1

            if len(self._history) >= 20:
                impose = True
                prev = None
                for i in range(len(self._history)):
                    if prev is None:
                        prev = self._history[i]["Invite"][dancer_id]
                    else:
                        if prev != self._history[i]["Invite"][dancer_id]:
                            impose = False
                        prev = self._history[i]["Invite"][dancer_id]
                if impose:
                    total_reward -= 5
                    #print(f"Танцор {dancer_id} навязывается!")

        else:
            total_reward -= 1

        # Partner's constancy
        if len(self._history) > 0:
            if self._history[-1]["Dance"][dancer_id] == action["Dance"] and action["Dance"] != -1:
                total_reward += 2

        # Drop any partners
        if len(self._history) > 0:
            if self._history[-1]["Dance"][dancer_id] != -1 and action["Dance"] == -1:
                total_reward -= 2

        # Accepting an invitation from any dancer
        if len(self._history) > 0:
            if dancer_id in self._history[-1]["Invite"]:
                if action["Dance"] == self._history[-1]["Invite"].index(dancer_id):
                    total_reward += 6
                    #print(f"Приглашение принято: от {self._history[-1]['Invite'].index(dancer_id)} к {dancer_id}")
                else:
                    total_reward -= 6
                    #print(f"Приглашение отклонено: от {self._history[-1]['Invite'].index(dancer_id)} к {dancer_id}")






        """
        # If the dancers form a pair, then the reward increases by 1
        if state["Dance"][action["Dance"]] == dancer_id:
            total_reward += 1

        # If the dancer forms a pair with himself, then the reward increases by. 1
        elif action["Dance"] == dancer_id:
            total_reward += 0.5

        # If the dancer does not form a mutual pair, then the reward is reduced by 1
        else:
            total_reward -= 1"""

        # Noise modulation
        if self._is_noise:
            if self._noise_type == "first_iterations":
                if self._iteration < self._noise_count:
                    total_reward = random.randint(-2, 2)

        self._iteration += 1
        self._history.append(state)

        return total_reward


if __name__ == "__main__":
    h = StateHistory(3)
    h.append(1)
    h.append(2)
    h.append(3)
    h.append(4)
