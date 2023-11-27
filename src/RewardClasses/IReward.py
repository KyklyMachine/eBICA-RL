class IReward:

    def reward(self, state, action, dancer_id):
        raise NotImplementedError()
