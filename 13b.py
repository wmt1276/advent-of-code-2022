import json
from aoc import get_input
from aocd import submit

day = 13

def compare(left, right) -> bool:
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
            result = compare(left[index], right[index])
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
        
def sort(data: list):
    middle = data[0]
    
    left = []
    right = []
    
    for entry in data[1:]:
        if compare(entry, middle) == True:
            left.append(entry)
        else:
            right.append(entry)
            
    if len(left) > 1:
        left = sort(left)
        
    if len(right) > 1:
        right = sort(right)
        
    return left + [middle] + right
    

def main(data: list):
    entries = [[[2]], [[6]]]
    for index in range(len(data)):   # Iterate Over Each Line in Data
        raw_entries = data[index].splitlines()
        
        entry_pair = [json.loads(raw_entry) for raw_entry in raw_entries]
        
        for entry in entry_pair:
            entries.append(entry)
            
    sorted_entries = sort(entries)
    
    first_index = sorted_entries.index([[2]]) + 1
    second_index = sorted_entries.index([[6]]) + 1

    return first_index * second_index

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
        submit(answer, part='b', day=day, year=2022)
    else:
        print('No Answer Submitted')