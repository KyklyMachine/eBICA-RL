import random as rnd
import numpy as np
import copy


def reward(s: str, a: str) -> float:

    if s == "Танцевать":
        if a == "Танцевать":
            return 1
        if a == "Не танцевать":
            return -1

    if s == "Не танцевать":
        if a == "Танцевать":
            return -1
        if a == "Не танцевать":
            return 0



class SimpleDancer:

    alpha = 0.1
    gamma = 0.5

    S = ["Танцевать", "Не танцевать"]   # пространство состояний   <- init
    s = None                            # текущее состояние        <- выбирается пользователем
    prev_s = None
    A = ["Танцевать", "Не танцевать"]   # пространство действий    <- init
    a: str                              # текущее действие         <- автоматически выбирается
    # p                                   функция переходов        <- выбирается пользователем (через функцию set_s)
    # r                                   функция награды          <- init
    Q = np.array(                       # Q значение               <- init
                    [
                        [0.0, 0.0],
                        [0.0, 0.0]
                    ]
                )
    r: staticmethod
    #
    # Q:       s\a       | "Танцевать",| "Не танцевать" |
    #    ----------------+--------------+---------------|
    #    "Танцевать"     |      q00     |      q01      |
    #    ----------------+--------------+---------------+
    #    "Не танцевать"  |      q10     |      q11      |
    #    ----------------+--------------+---------------+
    #
    #

    def __init__(self):
        # задаем функцию переходов
        self.p = self.set_s

        # задаем функцию награды
        self.r = reward


    def set_s(self):
        act_number = int(input("Введите номер действия:\n"
                                "   0 – Танцевать\n"
                                "   1 – Не танцевать\n"
                                "Ввод: "))
        if act_number not in [0, 1, 2]:
            print("Неверный номер действия! Повторите ввод.")
            return self.set_s()
        if self.s:
            self.prev_s = self.s
        self.s = self.S[act_number]

    def set_a(self):
        state_index = self.S.index(self.s)
        a_i = np.where(self.Q[state_index] == self.Q[state_index].max())[0][0]
        self.a = self.A[a_i]

    def update_Q(self):
        s_index = self.S.index(self.s)
        a_index = np.where(self.Q[s_index] == self.Q[s_index].max())[0][0]
        # evaluate Q:
        if self.prev_s:
            reward = self.r(self.prev_s, self.a)
            q_sa = ((1 - self.alpha) * self.Q[s_index, a_index] +
                    self.alpha * (reward + self.gamma * self.Q[s_index].max()))
            self.Q[s_index, a_index] = q_sa

    def iteration(self):
        self.set_s()
        self.update_Q()
        self.set_a()

        print(f"Бот выбрал {self.a}\n"
              f"Человек выбрал {self.s}")
        reward_bot = self.r(self.s, self.a)
        if reward_bot == -1:
            print("Вы в печали!")
        elif reward_bot == 1:
            print("Вы счастливы!")
        else:
            print("Пофиг?")


if __name__ == "__main__":
    rps = SimpleDancer()
    choice = "y"
    while choice == "y":
        rps.iteration()
        choice = input("Продолжить танцевать (y/n)?")
