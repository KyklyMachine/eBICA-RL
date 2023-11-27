

class ILearningModel:

    _alpha: float = 0.3
    _gamma: float = 0.5

    def fit(self, state, action, q_matrix, reward: float):
        raise NotImplementedError()