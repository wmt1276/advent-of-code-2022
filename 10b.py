from aoc import get_input
from aocd import submit

day = 10

def main(data: list):
    display = ''
    
    cycle = -1
    x = 1
    
    for line in data:   # Iterate Over Each Line in Data
        cycle += 1
        
        if cycle % 40 in range(x - 1, x + 2):
            display += '#'
        else:
            display += '.'
            
        if line != 'noop':
            cycle += 1
            
            if cycle % 40 in range(x - 1, x + 2):
                display += '#'
            else:
                display += '.'

            fields = line.split(' ')
            
            x += int(fields[1])
            
    output = ''
    
    for i in range(0, len(display), 40):
        output += display[i:i+40] + '\n'
            
    return output

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
#     data = '''addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop'''.splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    # if answer not in [None, '', 0]:
    #     submit(answer, part='b', day=day, year=2022)
    # else:
    #     print('No Answer Submitted')