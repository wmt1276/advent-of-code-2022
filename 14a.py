from aoc import get_input
from aocd import submit

day = 14

def print_cave(cave: list, min_x: int, max_x: int, max_y: int):
    for y in range(0, max_y + 2):
        for x in range(min_x, max_x + 1):
            print(cave[y][x], end='')
        print()
    print('\n')

def main(data: list):
    rock_symbol = '#'
    air_symbol = '.'
    sand_symbol = 'o'
    rocks = []
    max_x = 500
    max_y = 0
    min_x = 500
    
    for line in data:   # Iterate Over Each Line in Data
        # print(line)
        rock_line = line.split(' -> ')
        rocks_structure = []
        for rock in rock_line:
            coords = rock.split(',')
            
            x = int(coords[0])
            y = int(coords[1])
            
            if x > max_x:
                max_x = x
            elif x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
                
            coords = [x, y]
            rocks_structure.append(coords)
        rocks.append(rocks_structure)
        
    cave = [[air_symbol for _ in range((max_x + 1) * 2)] for _ in range(max_y + 2)]
    
    for rock in rocks:
        # print(rock)
        for line in range(1, len(rock)):
            start_coords = rock[line - 1][:]
            end_coords = rock[line][:]
            
            if start_coords[0] > end_coords[0]:
                start_coords[0], end_coords[0] = end_coords[0], start_coords[0]
                
            if start_coords[1] > end_coords[1]:
                start_coords[1], end_coords[1] = end_coords[1], start_coords[1]
            
            for x in range(start_coords[0], end_coords[0] + 1):
                for y in range(start_coords[1], end_coords[1] + 1):
                    cave[y][x] = rock_symbol
            # print_cave(cave, min_x, max_x, max_y)
                    
    # print_cave(cave)
                    
    sand_origin = [500, 0]
    
    cave[sand_origin[1]][sand_origin[0]] = '+'
                    
    full = False
    sand_count = 0
    
    while not full:
        sand_coords = sand_origin[:]
        
        while sand_coords[1] < max_y:
            if cave[sand_coords[1] + 1][sand_coords[0]] == air_symbol:
                sand_coords[1] += 1
            elif cave[sand_coords[1] + 1][sand_coords[0] - 1] == air_symbol:
                sand_coords[0] -= 1
                sand_coords[1] += 1
            elif cave[sand_coords[1] + 1][sand_coords[0] + 1] == air_symbol:
                sand_coords[0] += 1
                sand_coords[1] += 1
            else:
                break
            
        
        if cave[sand_coords[1] + 1][sand_coords[0]] == air_symbol:
            full = True
            break
        else:
            sand_count += 1
            cave[sand_coords[1]][sand_coords[0]] = sand_symbol
            # print_cave(cave, min_x, max_x, max_y)

    return sand_count

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
#     data = '''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')