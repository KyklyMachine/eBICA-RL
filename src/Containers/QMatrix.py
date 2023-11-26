import numpy as np
import pandas as pd


class QMatrix:

    # TODO: in the next version _matrix will be a tensor
    _matrix: pd.DataFrame

    def __init__(self, states: list, actions: list, values: np.array = None):
        if values is not None:
            self._matrix = pd.DataFrame(data=values, columns=actions, index=states)
        else:
            data0 = np.zeros(len(states) * len(actions)).reshape((len(states), len(actions)))
            self._matrix = pd.DataFrame(data=data0, index=states, columns=actions)

    @property
    def states(self):
        return self._matrix.index

    @property
    def actions(self):
        return self._matrix.columns

    @property
    def iloc(self):
        return self._matrix.iloc

    @property
    def loc(self):
        return self._matrix.loc

    def set(self, value, index_name, column_name):
        self._matrix.loc[index_name, column_name] = value

    def __str__(self):
        return str(self._matrix)


if __name__ == "__main__":
    states_list = ["A", "B", "C"]
    actions_list = [2, 3, 4]
    values_arr = np.array([
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 1]
    ])
    m = QMatrix(states_list, actions_list, values_arr)

    print(m)

