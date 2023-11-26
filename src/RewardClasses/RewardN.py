import random

from src.RewardClasses.IReward import IReward


class Reward(IReward):

    _is_first = True
    _is_second = True

    def __init__(self):
        pass

    def reward(self, state, action, dancer_id):

        """
        {'Invite': (2, 0, 0, 0), 'Dance': (1, 0, 0, 0)}
        {'Invite': 0, 'Dance': 0}
        """
        if self._is_first:
            self._is_first = False
            print(11111)
            return random.randint(-2, 2)

        if not self._is_first and self._is_second:
            self._is_second = False
            print(11111)
            return random.randint(-2, 2)

        total_reward = 0

        # если есть пара для танца - награда +1
        if action["Dance"] != dancer_id:
            if state["Dance"][action["Dance"]] == dancer_id:
                total_reward += 1
            elif action["Dance"] == dancer_id:
                total_reward += 0.5
            else:
                total_reward -= 0.5
        else:
            total_reward -= 1

        return total_reward

