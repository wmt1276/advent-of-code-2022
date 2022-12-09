from aoc import get_input
from aocd import submit
from copy import deepcopy

day = 8

def main(data: list) -> int:
    height = len(data)
    width = len(data[0])
    
    tree_heights = []
    
    for line in data:   # Iterate Over Each Line in Data
        row = []
        for tree in line:
            row.append(int(tree))
        tree_heights.append(row)
        
    max_visibility = 0
        
    for row in range(height):
        for col in range(width):
            block = tree_heights[row][col]
            visible = [0 for _ in range(4)]
            for r in range(row + 1, width):
                visible[0] += 1
                if tree_heights[r][col] >= block:
                    break
            for r in range(row - 1, -1, -1):
                visible[1] += 1
                if tree_heights[r][col] >= block:
                    break
            for c in range(col + 1, height):
                visible[2] += 1
                if tree_heights[row][c] >= block:
                    break
            for c in range(col - 1, -1, -1):
                visible[3] += 1
                if tree_heights[row][c] >= block:
                    break
            visibility = 1
            for score in visible:
                visibility *= score
            if visibility > max_visibility:
                max_visibility = visibility
                
    return max_visibility

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
        submit(answer, part='b', day=day, year=2022)
    else:
        print('No Answer Submitted')