from functools import cache
from aoc import get_input
from aocd import submit

day = 11

def inspect(item, monkey):
    if monkey == 0:
        item *= 5
    elif monkey == 1:
        item *= 11
    elif monkey == 2:
        item += 2
    elif monkey == 3:
        item += 5
    elif monkey == 4:
        item *= item
    elif monkey == 5:
        item += 4
    elif monkey == 6:
        item += 6
    elif monkey == 7:
        item += 7
        
    return item

@cache
def throw(item, monkey):
    if monkey == 0:
        if item % 11 == 0:
            return 2
        else:
            return 3
    elif monkey == 1:
        if item % 5 == 0:
            return 4
        else:
            return 0
    elif monkey == 2:
        if item % 19 == 0:
            return 5
        else:
            return 6
    elif monkey == 3:
        if item % 13 == 0:
            return 2
        else:
            return 6
    elif monkey == 4:
        if item % 7 == 0:
            return 0
        else:
            return 3
    elif monkey == 5:
        if item % 17 == 0:
            return 7
        else:
            return 1
    elif monkey == 6:
        if item % 2 == 0:
            return 7
        else:
            return 5
    elif monkey == 7:
        if item % 3 == 0:
            return 4
        else:
            return 1

def main():
    worry_catch = 11 * 5 * 19 * 13 * 7 * 17 * 2 * 3
    
    inspections = [0 for _ in range(8)]
    
    monkeys = [[83, 88, 96, 79, 86, 88, 70], [59, 63, 98, 85, 68, 72], [90, 79, 97, 52, 90, 94, 71, 70], [97, 55, 62], [74, 54, 94, 76], [58], [66, 63], [56, 56, 90, 96, 68]]
    
    for cycle in range(10000):
        for monkey in range(len(monkeys)):
            items = monkeys[monkey]
            
            item_count = len(items)
            
            inspections[monkey] += item_count
            for _ in range(item_count):
                
                item = items.pop(0)
                
                item = inspect(item, monkey)
                
                item %= worry_catch
                
                monkeys[throw(item, monkey)].append(item)

    top = max(inspections)
    
    inspections.remove(top)
    
    return max(inspections) * top

if __name__ == '__main__':
    answer = main()
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='b', day=day, year=2022)
    else:
        print('No Answer Submitted')