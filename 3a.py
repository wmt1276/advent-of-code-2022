from aoc import get_input
from aocd import submit

def priotiy(item):
    # Returns Priority Score of Item Based on Character
    if item < '[':
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1
    
def multiplicity(rucksack):
    # Finds Item in Both Rucksack Compartments
    
    # Split Rucksack Compartments
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    
    # Find Item in Both Compartments
    for item in first:
        if item in second:
            return item

def main(data: list) -> int:
    priotities = 0
    for line in data:   # Iterate Over Each Line in Data
        priotities += priotiy(multiplicity(line))

    return priotities

if __name__ == '__main__':
    # Get Input Data
    data = get_input(3).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=3, year=2022)
    else:
        print('No Answer Submitted')