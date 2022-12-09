from aoc import get_input
from aocd import submit

def main(data) -> int:
    for i in range(4, len(data)):
        substring = data[i-4:i]
        
        duplicate = False
        for char in substring:
            if substring.count(char) > 1:
                duplicate = True
                
        if not duplicate:
            return i

if __name__ == '__main__':
    # Get Input Data
    data = get_input(6)
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=6, year=2022)
    else:
        print('No Answer Submitted')