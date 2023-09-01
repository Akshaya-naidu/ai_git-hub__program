#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    ix = 0
    iy = 0
    fx = 0
    fy = 0
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':  # Find initial position
                ix = i
                iy = j
            elif grid[i][j] == 'p':  # Find princess position
                fx = i
                fy = j
    
    if fx > ix:
        for k in range(fx - ix):
            print("DOWN")
    else:
        for k in range(ix - fx):
            print("UP")
    
    if fy > iy:
        for k in range(fy - iy):
            print("RIGHT")
    else:
        for k in range(iy - fy):
            print("LEFT")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
