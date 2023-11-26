from src.RewardClasses.IReward import IReward


class Reward(IReward):

    def __init__(self):
        super().__init__()

    @staticmethod
    def reward(self, state, action):
        pass