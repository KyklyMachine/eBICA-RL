import random

from src.RewardClasses.IReward import IReward


class Reward(IReward):

    _is_first = True
    _is_second = True
    _is_noise: bool
    _noise_type: str
    _noise_count: int
    _iteration: int = 0

    def __init__(self):
        pass

    def reward(self, state, action, dancer_id, noise=True, noise_type="first_iterations", noise_count=2):

        self._is_noise = noise
        self._noise_type = noise_type
        self._noise_count = noise_count

        total_reward = 0

        # If the dancers form a pair, then the reward increases by 1
        if state["Dance"][action["Dance"]] == dancer_id:
            total_reward += 1

        # If the dancer forms a pair with himself, then the reward increases by. 1
        elif action["Dance"] == dancer_id:
            total_reward += 0.5

        # If the dancer does not form a mutual pair, then the reward is reduced by 1
        else:
            total_reward -= 1

        if self._is_noise:
            if self._noise_type == "first_iterations":
                if self._iteration < self._noise_count:
                    total_reward = random.randint(-2, 2)

        self._iteration += 1

        return total_reward

