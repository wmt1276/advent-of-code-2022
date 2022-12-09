from aoc import get_input
from aocd import submit

day = 7

def get_size(file_structure: dict, file: str) -> int:
    if type(file_structure[file][1]) == int:
        return file_structure[file][1]
    else:
        size = 0
        for f in file_structure[file][1]:
            size += get_size(file_structure, f)
        return size

def main(data: list) -> int:
    file_structure = {'/': ('/', [])}
    cursor = '/'
    for line in data:   # Iterate Over Each Line in Data
        if line[0] == '$':
            line = line[2:]
            
            if line[0:2] == 'cd':
                line = line[3:]
                
                if line == '..':
                    cursor = file_structure[cursor][0]
                else:
                    if line == '/':
                        cursor = '/'
                    else:
                        cursor = cursor + '/' + line
                
            elif line[0:2] == 'ls':
                continue
        else:
            fields = line.split(' ')
            size = fields[0]
            if size == 'dir':
                size = []
            else:
                size = int(size)
            filename = cursor + '/' + fields[1]
            file_structure[filename] = (cursor, size)
            file_structure[cursor][1].append(filename)

    total = 0
    for key in file_structure.keys():
        if type(file_structure[key][1]) == int:
            continue
        size = get_size(file_structure, key)
        if size < 100000:
            total += size
    return total

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