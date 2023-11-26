from src.RewardClasses.IReward import IReward


class Reward(IReward):

    def __init__(self):
        pass

    def reward(self, state, action):
        if action["Dance"] == 2 and action["Invite"] == 1:
            return 1
        else:
            return -1
