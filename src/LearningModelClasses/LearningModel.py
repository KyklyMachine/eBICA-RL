import copy

from src.LearningModelClasses.ILearningModel import ILearningModel


class LearningModel(ILearningModel):

    _s_prev: dict[str: tuple] = None

    def __init__(self, alpha=0.2, gamma=0.5):
        self._alpha = alpha
        self._gamma = gamma

    def fit(self, state: dict[str: tuple], action: dict[str: int], q_matrix, reward: float = 0):

        new_q = copy.deepcopy(q_matrix)

        if self._s_prev:
            q = {}
            for val in state.keys():
                s_new = state[val]
                a_new = action[val]
                q_matrix_val = q_matrix[val]
                q[val] = ((1 - self._alpha) * q_matrix_val.loc[[s_new]][a_new].values[0] +
                        self._alpha * (reward + self._gamma * q_matrix_val.loc[[s_new]].to_numpy().max()))
                new_q[val].set(q[val], [self._s_prev[val]], action[val])
            self._s_prev = state
            return new_q
        else:
            self._s_prev = {}
            for val in state.keys():
                s_new = state[val]
                self._s_prev[val] = s_new
            return q_matrix
