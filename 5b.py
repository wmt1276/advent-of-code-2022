from aoc import get_input
from aocd import submit

def main(data: list) -> int:
    stacks = [['R', 'G', 'J', 'B', 'T', 'V', 'Z'], ['J', 'R', 'V', 'L'], ['S', 'Q', 'F'], ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'], ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'], ['S', 'W', 'T', 'C', 'H', 'F'], ['D', 'Z', 'C', 'V', 'F', 'N', 'J'], ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'], ['J', 'B', 'W', 'V', 'P']]
    
    empty = False
    for line in data:   # Iterate Over Each Line in Data
        if not empty:
            if line == '':
                empty = True
        else:
            commands = line.split(' ')
            amount = int(commands[1])
            origin = int(commands[3]) - 1
            destination = int(commands[5]) - 1
            
            moved = stacks[origin][-amount:]
            
            stacks[destination] += stacks[origin][-amount:]
            
            stacks[origin] = stacks[origin][:-amount]
            
    output = ''
    for stack in stacks:
        output += stack.pop()

    return output

if __name__ == '__main__':
    # Get Input Data
    data = get_input(5).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='b', day=5, year=2022)
    else:
        print('No Answer Submitted')