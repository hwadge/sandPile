import numpy
import matplotlib.pyplot as plt
import math

avalancheList = []

def InstantiateGrid(dim):
    grid = numpy.zeros((dim,dim))
    return grid

def SandDropper(x, y, grid):
    grid[x][y] = grid[x][y] + 1

def iterate(grid):
    changed = False
    avalanche = 0
    global avalancheList
    for ii, arr in enumerate(grid):
        for jj, val in enumerate(arr):
            if val > 3:
                grid[ii, jj] -= 4
                if ii > 0:
                    grid[ii - 1, jj] += 1
                    avalanche = avalanche + 1
                if ii < len(grid)-1:
                    grid[ii + 1, jj] += 1
                    avalanche = avalanche + 1
                if jj > 0:
                    grid[ii, jj - 1] += 1
                    avalanche = avalanche + 1
                if jj < len(grid)-1:
                    grid[ii, jj + 1] += 1
                    avalanche = avalanche + 1
                changed = True
    avalancheList.append(avalanche)
    return grid, changed

def simulate(grid):
    while True:
        grid, changed = iterate(grid)
        if not changed:
            return grid

def main():
    N = 10000
    dim = 50
    global avalancheList
    grid = InstantiateGrid(dim)

    for j in range(N):
        SandDropper(math.ceil(dim/2), math.ceil(dim/2), grid)
        grid2 = simulate(grid)
    
    plt.subplot(1, 2, 1)
    plt.hist(avalancheList)

    plt.subplot(1, 2, 2)
    plt.imshow(grid2)
    plt.show()


if __name__ == "__main__":
    main()