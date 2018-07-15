from __future__ import division
import math
from math import*
import operator
import collections
import numpy as np


def validation(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def euclideanDistance(instance1, instance2):
    hasil = math.sqrt(sum(np.subtract(np.array(instance1), np.array(instance2)) ** 2))
    return hasil


def pearson_correlation(a, b):
    x_squared = [(x**2) for x in a]
    y_squared = [(x ** 2) for x in b]
    tot_xy = [x*y for x,y in zip(a,b)]
    up = sum(tot_xy) - (sum(a) * sum(b) / len(a))
    x = sum(x_squared) - ((sum(a) ** 2) / len(a))
    y = sum(x_squared) - ((sum(b) ** 2) / len(a))
    down = sqrt(x*y)
    return float(up/down)
    # except ZeroDivisionError:
    #     return 0
    # return result


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(np.array(x))*square_rooted(np.array(y))
    try:
        return round(numerator/float(denominator),3)
    except ZeroDivisionError:
        return 0


def get_neighbourhood(simm_euclid, target_train, pnn):
    jarakKlas = []
    for b in range(2):  # [0,1]
        tmp_jarakKlas = []
        value_a = []
        for c in range(len(simm_euclid)):
            if target_train[c] == b:
                tmp_jarakKlas.append(simm_euclid[c])
        tmp_jarakKlas.sort()
        value_a.sort()
        for line in tmp_jarakKlas[:pnn]:
            jarakKlas.append([b, line])
    b = {}
    for x in jarakKlas: b.setdefault(x[0], []).append(x[1])
    avgDict = {}
    x = 1
    for k, v in b.items():
        avgDict[k] = sum((1.0 / i) * g for i, g in enumerate(v, 1))
        x += 1
    min_index, min_value = min(avgDict.items(), key=lambda x: x[1])  # untuk mendapatkan min. index
    return min_index, min_value


def hammingloss(selisih, jumlah_testing):
    nilai = jumlah_testing * 16
    hammingloss_label = (float(1 / (nilai)) * selisih)
    return hammingloss_label