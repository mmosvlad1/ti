import numpy as np

p_xy = np.array([[0.105, 0.025, 0.120],
                 [0.030, 0.175, 0.060],
                 [0.015, 0.050, 0.420]])


def entropy(p):
    return -np.sum(p * np.log2(p))


def p_x():
    return np.sum(p_xy, axis=0)


def p_y():
    return np.sum(p_xy, axis=1)


def p_y_given_x():
    return p_xy / p_x()


def mutual_information():
    return entropy(p_x()) + entropy(p_y()) - entropy(p_xy)


def max_information_y():
    return np.log2(p_xy.shape[1])


def capacity():
    return max_information_y() - entropy(p_y_given_x()[0])


print(f"Взаємна інформація: {mutual_information()}")
print(f"Пропускна здатність каналу: {capacity()}")
