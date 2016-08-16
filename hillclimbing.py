from problem import inputMatrix

def calculateDistance(path,distanceMatrix):
	index = path[0]
	distance = 0
	for nextIndex in path[1:]:
		distance += distanceMatrix[index][nextIndex]
		index = nextIndex
	return distance+distanceMatrix[path[-1]][path[0]];

def swap(sequence,i,j):
	temp = sequence[i]
        sequence[i]=sequence[i+1]
        sequence[i+1]=temp

improvements = True
distanceMatrix = inputMatrix
n = len(distanceMatrix)
path = range(0,n,1)
bestPath = path[:]
distance = calculateDistance(path,distanceMatrix)
while(improvements):
	improvements = False;
	for i in range(n-1):
		swap(path,i,i+1)
		newDistance = calculateDistance(path,distanceMatrix);
		if(distance>newDistance):
			improvements = True
			bestPath = path[:]
			distance = newDistance;
		else:
			swap(path,i,i+1)

print "HILL CLIMBING"
print "PATH :"
print bestPath
print "DISTANCE :"
print distance
