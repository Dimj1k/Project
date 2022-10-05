from numpy import linspace, pi, sin, cos, sqrt, array
from pandas.plotting import parallel_coordinates
from pandas.plotting import radviz


class AndrewsCurve:

    @staticmethod
    def __sin_cos(n: int, th: array) -> array:
        return cos(th) if n % 2 else sin(th)

    def __init__(self) -> None:
        self.theta = linspace(-pi, pi, 1000)

    def curves(self, X: array) -> array:
        if len(X[0]) < 2:
            raise IndexError(f"Введите больше 2 X i-тых в одну строчку. Сейчас их {len(X[0])}")
        for x in X:
            yield x[0] / sqrt(2) + sum([x[i - 1] * (self.__sin_cos(i, (i // 2) * self.theta))
                                        for i in range(2, len(x) + 1)])
