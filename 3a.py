from aoc import get_input
from aocd import submit

def main(data: list) -> int:
    for line in data:   # Iterate Over Each Line in Data
        print(line)

    return None

if __name__ == '__main__':
    # Get Input Data
    data = get_input(3).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer)
    else:
        print('No Answer Submitted')