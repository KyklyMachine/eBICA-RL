class IReward:
    def __init__(self):
        raise NotImplementedError()

    @staticmethod
    def reward(self, state, action):
        raise NotImplementedError()