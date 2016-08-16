from problem import inputMatrix
from random import uniform
from random import randint 
import math


distanceMatrix = inputMatrix

def levyFlight(u):
	return math.pow(u,-1.0/3.0)

def randF():
	return uniform(0.0001,0.9999)

def calculateDistance(path):
        index = path[0]
        distance = 0
        for nextIndex in path[1:]:
                distance += distanceMatrix[index][nextIndex]
                index = nextIndex
        return distance+distanceMatrix[path[-1]][path[0]];

def swap(sequence,i,j):
        temp = sequence[i]
        sequence[i]=sequence[j]
        sequence[j]=temp

def twoOptMove(nest,a,c):
	nest = nest[0][:]
	swap(nest,a,c)
	return (nest,calculateDistance(nest))
	

def doubleBridgeMove(nest,a,b,c,d):
	nest = nest[0][:]
	swap(nest,a,b)
	swap(nest,b,d)
	return (nest , calculateDistance(nest))

def hillClimbing(sequence):
	improvements = True
	distanceMatrix = inputMatrix
	n = len(distanceMatrix)
	path = sequence[0][:]
	bestPath = path[:]
	distance = calculateDistance(path)
	while(improvements):
		improvements = False;
		for i in range(n-1):
			swap(path,i,i+1)
			newDistance = calculateDistance(path);
			if(distance>newDistance):
				improvements = True
				bestPath = path[:]
				distance = newDistance;
			else:
				swap(path,i,i+1)
	return (bestPath,calculateDistance(bestPath))


numNests = 10
pa = int(0.2*numNests)
pc = int(0.6*numNests)

maxGen = 50

n = len(inputMatrix)

nests = []

initPath=range(0,n)
index = 0
for i in range(numNests):
	if index == n-1:
		index = 0
	swap(initPath,index,index+1)
	index+=1
	nests.append((initPath[:],calculateDistance(initPath)))

nests.sort(key=lambda tup: tup[1])

for t in range(maxGen):
	cuckooNest = nests[randint(0,pc)]
	if(levyFlight(randF())>2):
		if(randint(0,1)==1):
			cuckooNest = doubleBridgeMove(cuckooNest,randint(0,n-1),randint(0,n-1),randint(0,n-1),randint(0,n-1))
		else:
			cuckooNest = hillClimbing(cuckooNest)
	else:
		cuckooNest = twoOptMove(cuckooNest,randint(0,n-1),randint(0,n-1))
	randomNestIndex = randint(0,numNests-1)
	if(nests[randomNestIndex][1]>cuckooNest[1]):
		nests[randomNestIndex] = cuckooNest
	for i in range(numNests-pa,numNests):
		nests[i] = twoOptMove(nests[i],randint(0,n-1),randint(0,n-1))
	nests.sort(key=lambda tup: tup[1])

print "CUCKOO's SOLUTION"	
print(nests[0])

