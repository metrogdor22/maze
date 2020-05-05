

maze = [[0,0,0,0,1,0,0,0,0,0],
		[1,1,1,0,1,1,1,0,1,0],
		[1,0,1,0,0,0,1,0,1,0],
		[1,0,1,1,1,0,1,0,1,1],
		[1,0,0,0,0,0,1,0,0,0],
		[0,0,1,0,1,1,1,0,1,0],
		[1,0,1,0,0,0,0,0,1,0],
		[0,0,1,0,1,1,1,1,1,0],
		[0,1,1,0,1,0,0,1,1,0],
		[0,1,1,0,0,0,1,1,1,2]]

# Returns the left, up, right, down neighbors
def getNeighbors(array,x,y):
	return (array[x][y-1], array[x-1][y], array[x][y+1], array[x+1][y])

print(getNeighbors(maze,3,3))