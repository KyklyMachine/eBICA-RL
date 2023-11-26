class IReward:
    def __init__(self):
        raise NotImplementedError()

    def reward(self, state, action):
        raise NotImplementedError()