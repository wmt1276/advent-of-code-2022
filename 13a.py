import json
from aoc import get_input
from aocd import submit

day = 13

def compare(right, left) -> bool:
    right_type = type(right)
    left_type = type(left)
    
    if right_type != left_type:
        if right_type == int:
            right = [right]
        else:
            left = [left]
            
    if type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    else:
        result = None
        index = 0
        while result == None and index < len(right) and index < len(left):
            result = compare(right[index], left[index])
            index += 1
        if result == None:
            if len(right) > len(left):
                return True
            elif len(right) < len(left):
                return False
            else:
                return None
        else:
            return result

def main(data: list):
    correct = []
    for index in range(len(data)):   # Iterate Over Each Line in Data
        raw_entries = data[index].splitlines()
        
        entries = [json.loads(raw_entry) for raw_entry in raw_entries]
        
        if compare(entries[1], entries[0]) == True:
            correct.append(index + 1)

    return sum(correct)

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).split('\n\n')
    
#     data = '''[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n\n')
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')