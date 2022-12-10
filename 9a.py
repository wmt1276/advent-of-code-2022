from aoc import get_input
from aocd import submit

day = 9

def catch_up(head, tail):
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1])

    if distance == 2:
        if head[0] == tail[0]:
            if head[1] > tail[1] + 1:
                tail[1] += 1
            elif head[1] < tail[1] - 1:
                tail[1] -= 1
        elif head[1] == tail[1]:
            if head[0] > tail[0] + 1:
                tail[0] += 1
            elif head[0] < tail[0] - 1:
                tail[0] -= 1
    elif distance > 2:
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
            
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
            
    return tail

def move(head, tail, direction):
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1
        
    tail = catch_up(head, tail)
        
    return head, tail

def main(data: list):
    visited = {(0, 0)}
    head = [0, 0]
    tail = [0, 0]
    for line in data:   # Iterate Over Each Line in Data
        fields = line.split(' ')
        times = int(fields[1])
        
        for _ in range(times):
            head, tail = move(head, tail, fields[0])
            
            visited.add((tail[0], tail[1]))

    return len(visited)

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