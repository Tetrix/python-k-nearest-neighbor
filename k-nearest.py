import csv
import math
import operator
import random
import os



def separate_data(filepath, size, train_set=[] , test_set=[]):
	test_data=[]
	train_data=[]
	with open(filepath, 'r') as data:
	    lines = csv.reader(data)
	    dataset = list(lines)

	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < size:
	            train_set.append(dataset[x])
	        else:
	            test_set.append(dataset[x])
	return train_set, test_set



def euclidean_distance(train_set, test_set, length):
	distance=0
	for i in range (length):
		if test_set and train_set:
			distance += pow((float(train_set[i]) - float(test_set[i])),2)
	return math.sqrt(distance)



def get_neighbors(train_set, test_set, k):
	distance = []
	length=len(test_set)-2
	for i in range(len(train_set)):
		euclid = euclidean_distance(test_set, train_set[i], length)
		distance.append((train_set[i], euclid))

	distance.sort(key=operator.itemgetter(1))	
	neighbors = []
	for i in range(k):
		neighbors.append(distance[i][0])
	return neighbors	




def get_value(neighbors):
	items = {}
	for i in range(len(neighbors)):
		value = neighbors[i][-1]
		if value in items:
			items[value] += 1
		else:
			items[value] = 1

	winner = sorted(items.items(), key=operator.itemgetter(1))
	return winner[-1][0]	





def main():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	filepath = os.path.join(current_dir, 'data', 'iris_data.csv')
	train_set, test_set =  separate_data(filepath, 0.7)
	hit = 0
	miss = 0
	for i in range(len(test_set)-1):
		neighbors = get_neighbors(train_set, test_set[i], 3)
		result = get_value(neighbors)
		print(' PREDICTED VALUE = ' + result + ', TRUE VALUE = ' + test_set[i][-1])
		
		if result == test_set[i][-1]:
			hit += 1
		else:
			miss +=1

	print('\n' + '  TOTAL HITS = ' + str(hit) + ' ------------------------------------------ TOTAL MISSES = ' + str(miss))

main()		