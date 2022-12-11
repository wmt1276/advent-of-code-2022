from aoc import get_input
from aocd import submit

day = 10

def main(data: list):
    cycle = 0
    x = 1
    
    check = range(20, 221, 40)
    
    strength = 0
    
    for line in data:   # Iterate Over Each Line in Data
        cycle += 1
        
        if cycle in check:
            strength += x * cycle
            
        if line != 'noop':
            cycle += 1
            
            if cycle in check:
                strength += x * cycle

            fields = line.split(' ')
            
            x += int(fields[1])
            
    return strength

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