from aoc import get_input
from aocd import submit

def main(data: list) -> int:
    contains = 0
    for line in data:   # Iterate Over Each Line in Data
        assignments = line.split(',')   #separate Elf Assignment Pairs
        
        # Get Ends of Each Assignment
        ends = []
        for assignment in assignments:
            end = assignment.split('-')
            nums = [int(x) for x in end]
            ends.append(nums)
            
        # Check if One Assignment Contains the Other
        if (ends[0][0] <= ends[1][1] and ends[0][1] >= ends[1][1]) or (ends[0][1] >= ends[1][0] and ends[0][1] <= ends[1][1]):
            contains += 1

    return contains

if __name__ == '__main__':
    # Get Input Data
    data = get_input(4).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='b', day=4, year=2022)
    else:
        print('No Answer Submitted')