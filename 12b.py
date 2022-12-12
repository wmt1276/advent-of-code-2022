from aoc import get_input
from aocd import submit

day = 12

def main(data: list):
    for line in data:   # Iterate Over Each Line in Data
        print(line)

    return None

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