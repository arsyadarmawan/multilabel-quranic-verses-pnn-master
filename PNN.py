import csv
import random
import math
import operator
import collections

def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def k(trainingSet, testInstance):
	test = separateByClass(testInstance)
	separated = separateByClass(trainingSet)
	summary = {}
	distances = []
	length = len(testInstance)-1
	for y in range(len(test)):
		for x in range(len(separated)):
			summary[x] = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append(trainingSet[x][-1], summary)
	return distances

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(testInstance)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x][-1], dist))
	return distances
	# distances.sort(key=operator.itemgetter(1))
	# list = {}
	# for x in distances: list.setdefault(x[0],[]).append(x[1]) #membagi bedasarkan kelas kelas dictionary
	# hasil = []
	# for f in range(len(list)):
	# 	for x in range(k):
	# 		hasil.append(list[f][x] * 1/(x+1))  #dari dictionary melalui pembobotan disimpan pada list
	# temp = [sum(hasil[i:i+k]) for i in range(0, len(hasil), k)]
	# return temp, distances[0][0]

def getkelas(neighbours):
	min_index, min_value = min(enumerate(neighbors[0]), key=operator.itemgetter(1))
	nilai = 0
	if (min_index == neighbors[1]):
		nilai += 1
	return nilai


if __name__ == '__main__':
	filename = 'indian.csv'
	dataset = loadCsv(filename)
	splitRatio = 0.67
	train, test = splitDataset(dataset, splitRatio)
	testing = separateByClass(test)
	print(('Split {0} rows into train with {1} and test with {2}').format(len(dataset), len(train), len(test)))
	print ""
	p = 2
	nilai = []
	for x in range(len(test)):
		neighbors = getNeighbors(train, test[x],p)
		print neighbors
	# 	kelas = getkelas(neighbors)
	# 	print neighbors
	# 	nilai.append(kelas)
	# hasil = sum(nilai)/float(len(test)) * 100,"%"
	# print "Akurasi ", hasil
