#!/usr/bin/env python
# coding: utf-8

# In[7]:


def print_sudoku(grid):
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=" ")
        print()

def is_valid(grid, row, col, num):
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_sudoku(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def arrange_sudoku(input_values):
    if len(input_values) != 16:
        print("Input should contain exactly 16 values.")
        return

    grid = [[0] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            grid[i][j] = input_values[i * 4 + j]

    print("Input:")
    print_sudoku(grid)

    if solve_sudoku(grid):
        print("\nArranged Sudoku-like grid:")
        print_sudoku(grid)
    else:
        print("\nNo solution exists for the given input values.")
input_values=[]
for i in range(0,16):
    x=int(input('Enter a Number:'))
    if x>-1 and x<5:
        input_values.append(x)
    else:
        print("Enter valid No.:")
arrange_sudoku(input_values)


# In[ ]:




