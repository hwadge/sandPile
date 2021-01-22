import numpy
import matplotlib.pyplot as plt
import math

def InstantiateGrid(dim):
    grid = numpy.zeros((dim,dim))
    return grid

def SandDropper(x, y, grid):
    grid[x][y] = grid[x][y] + 1

def iterate(grid, dim):
    avalanche = 0

    while numpy.max(grid) >= 4:

        avalanche = grid >= 4
        grid[avalanche] -= 4
        
        grid[1:,:][avalanche[:-1,:]] += 1
        grid[:-1,:][avalanche[1:,:]] += 1
        grid[:,1:][avalanche[:,:-1]] += 1
        grid[:,:-1][avalanche[:,1:]] += 1

        grid[0:1,:] = 0
        grid[1+dim[0]:,:] = 0
        grid[:,0:1] = 0
        grid[:,1+dim[1]:] = 0
	
    return grid

def main():
    N = 10000
    dim = (100,100)
    n = 0

    grid = InstantiateGrid(dim[0])
    
    while n < N:
        SandDropper(math.ceil(dim[0]/2), math.ceil(dim[0]/2), grid)
        grid2 = iterate(grid, dim)
        n += 1
        
    plt.imshow(grid2)
    plt.show()


if __name__ == "__main__":
    main()