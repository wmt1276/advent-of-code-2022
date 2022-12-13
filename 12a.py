from aoc import get_input
from aocd import submit

day = 12

def main(data: list):
    height_map = []
    cursor = (0, 0)
    goal = (0, 0)
    
    for row in range(len(data)):   # Iterate Over Each Line in Data
        line = data[row]
        
        heights = []
        for col in range(len(line)):
            char = line[col]
            
            if char == 'S':
                cursor = (row, col)
                heights.append(0)
            elif char == 'E':
                goal = (row, col)
                heights.append(ord('z') - ord('a'))
            else:
                heights.append(ord(char) - ord('a'))
        height_map.append(heights)
                
    queue = [cursor]
    visited = {cursor: 0}
    
    while goal not in visited:
        consider = queue.pop(0)
        
        if consider[0] > 0:
            up = (consider[0] - 1, consider[1])
            if up not in visited and height_map[up[0]][up[1]] <= height_map[consider[0]][consider[1]] + 1:
                queue.append(up)
                visited[up] = visited[consider] + 1
        if consider[0] < len(height_map) - 1:
            down = (consider[0] + 1, consider[1])
            if down not in visited and height_map[down[0]][down[1]] <= height_map[consider[0]][consider[1]] + 1:
                queue.append(down)
                visited[down] = visited[consider] + 1
        if consider[1] > 0:
            left = (consider[0], consider[1] - 1)
            if left not in visited and height_map[left[0]][left[1]] <= height_map[consider[0]][consider[1]] + 1:
                queue.append(left)
                visited[left] = visited[consider] + 1
        if consider[1] < len(height_map[0]) - 1:
            right = (consider[0], consider[1] + 1)
            if right not in visited and height_map[right[0]][right[1]] <= height_map[consider[0]][consider[1]] + 1:
                queue.append(right)
                visited[right] = visited[consider] + 1

    return visited[goal]

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')