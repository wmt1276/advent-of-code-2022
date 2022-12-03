from aoc import get_input
from aocd import submit

def priotiy(item):
    # Returns Priority Score of Item Based on Character
    if item < '[':
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1
        
def find_badges(data: list) -> str:
    # Find Badge Item in All Rucksacks
    for char in data[0]:
        if char in data[1] and char in data[2]:
            return char

def main(data: list) -> int:
    priotities = 0
    
    i = 0
    rucksacks = []
    for line in data:   # Iterate Over Each Line in Data
        rucksacks.append(line)
        
        i += 1
        
        if i == 3:
            badge = find_badges(rucksacks)
            
            priotities += priotiy(badge)
            
            i = 0
            rucksacks = []

    return priotities

if __name__ == '__main__':
    # Get Input Data
    data = get_input(3).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='b', day=3, year=2022)
    else:
        print('No Answer Submitted')