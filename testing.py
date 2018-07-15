import numpy as np
import math

def manhattan_distance(instance1, instance2, length):
    jarak = []
    for x in range(length):
        jarak.append(math.fabs(sum(np.subtract(np.array(instance1), np.array(instance2[x])))))
    return jarak

def cosine_similarity(v1, v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i];
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)



from math import*

def square_rooted(x):

    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):

    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)



a = [5,0,3,0,2,0,0,2,0,0]
b = [3,0,2,0,1,1,0,1,0,1]

def euclideanDistance(instance1, instance2):
    hasil = math.sqrt(sum(np.subtract(np.array(instance1), np.array(instance2)) ** 2))
    return hasil



x = [85,60,45,82,70,80,57,72,60,65]
y = [9,5,3,9,7,8,5,4,7,6]


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(np.array(x))*square_rooted(np.array(y))
    return round(numerator/float(denominator),3)

print cosine_similarity(x,y)
