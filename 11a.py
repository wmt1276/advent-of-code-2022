from aoc import get_input
from aocd import submit

day = 11

def main(data: list):
    inspections = [0 for _ in range(8)]
    
    monkeys = [[83, 88, 96, 79, 86, 88, 70], [59, 63, 98, 85, 68, 72], [90, 79, 97, 52, 90, 94, 71, 70], [97, 55, 62], [74, 54, 94, 76], [58], [66, 63], [56, 56, 90, 96, 68]]
    
    for _ in range(20):
        for monkey in range(len(monkeys)):
            items = monkeys[monkey]
            
            item_count = len(items)
            for _ in range(item_count):
                inspections[monkey] += 1
                
                item = items.pop(0)
                
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
                
                item = item // 3
                
                if monkey == 0:
                    if item % 11 == 0:
                        monkeys[2].append(item)
                    else:
                        monkeys[3].append(item)
                elif monkey == 1:
                    if item % 5 == 0:
                        monkeys[4].append(item)
                    else:
                        monkeys[0].append(item)
                elif monkey == 2:
                    if item % 19 == 0:
                        monkeys[5].append(item)
                    else:
                        monkeys[6].append(item)
                elif monkey == 3:
                    if item % 13 == 0:
                        monkeys[2].append(item)
                    else:
                        monkeys[6].append(item)
                elif monkey == 4:
                    if item % 7 == 0:
                        monkeys[0].append(item)
                    else:
                        monkeys[3].append(item)
                elif monkey == 5:
                    if item % 17 == 0:
                        monkeys[7].append(item)
                    else:
                        monkeys[1].append(item)
                elif monkey == 6:
                    if item % 2 == 0:
                        monkeys[7].append(item)
                    else:
                        monkeys[5].append(item)
                elif monkey == 7:
                    if item % 3 == 0:
                        monkeys[4].append(item)
                    else:
                        monkeys[1].append(item)

    top = max(inspections)
    
    inspections.remove(top)
    
    return max(inspections) * top

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')