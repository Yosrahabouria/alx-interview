#!/usr/bin/python3
"""
This file defines the function calculate_island_perimeter.
"""


def adjacent_land_cells(grid, x, y):
    """calculates the number of adjacent
    land cells."""
    adjacent_count = 0
    num_rows = len(grid)
    num_columns = len(grid[0])
    
    if (x > 0 and grid[x-1][y] == 1):
        adjacent_count += 1
    if (y > 0 and grid[x][y-1] == 1):
        adjacent_count += 1
    if (x < num_rows-1 and grid[x+1][y] == 1):
        adjacent_count += 1
    if (y < num_columns-1 and grid[x][y+1] == 1):
        adjacent_count += 1
    
    return adjacent_count


def island_perimeter(grid):
    """returns the perimeter of an island
    follwing the grid."""
    perimeter_total = 0
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                perimeter_total += 4 - adjacent_land_cells(grid, x, y)
    
    return perimeter_total
