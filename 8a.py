from aoc import get_input
from aocd import submit
from copy import deepcopy

day = 8

def main(data: list) -> int:
    height = len(data)
    width = len(data[0])
    
    visible = [[False for _ in range(width)] for _ in range(height)]
    tree_heights = []
    
    for line in data:   # Iterate Over Each Line in Data
        row = []
        for tree in line:
            row.append(int(tree))
        tree_heights.append(row)
        
    for row in range(height):
        trees = deepcopy(tree_heights[row])
        block = trees[0] - 1
        
        for col in range(width):
            if trees[col] > block:
                visible[row][col] = True
                block = trees[col]
                
        trees.reverse()
        block = trees[0] - 1
        for col in range(width):
            if trees[col] > block:
                visible[row][width - col - 1] = True
                block = trees[col]
                
    for col in range(width):
        trees = [row[col] for row in tree_heights]
        block = trees[0] - 1
        
        for row in range(height):
            if trees[row] > block:
                visible[row][col] = True
                block = trees[row]
                
        trees.reverse()
        block = trees[0] - 1
        for row in range(height):
            if trees[row] > block:
                visible[height - row - 1][col] = True
                block = trees[row]
                
    visible_count = 0
    
    for row in visible:
        for col in row:
            if col:
                visible_count += 1

    return visible_count

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
#     data = '''30373
# 25512
# 65332
# 33549
# 35390'''.splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')