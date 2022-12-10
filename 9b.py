from aoc import get_input
from aocd import submit

day = 9

def catch_up(knots):
    if len(knots) <= 1:
        return knots
    else:
        head = knots[0]
        tail = knots[1]
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
                
        knots[1] = tail
        
        knots = knots[:1] + catch_up(knots[1:])
                
        return knots

def move(knots, direction):
    if direction == 'U':
        knots[0][1] += 1
    elif direction == 'D':
        knots[0][1] -= 1
    elif direction == 'R':
        knots[0][0] += 1
    elif direction == 'L':
        knots[0][0] -= 1
        
    return catch_up(knots)

def main(data: list):
    visited = {(0, 0)}
    knots = [[0, 0] for _ in range(10)]
    for line in data:   # Iterate Over Each Line in Data
        fields = line.split(' ')
        times = int(fields[1])
        
        for _ in range(times):
            knots = move(knots, fields[0])
            
            visited.add((knots[-1][0], knots[-1][1]))

    return len(visited)

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='b', day=day, year=2022)
    else:
        print('No Answer Submitted')