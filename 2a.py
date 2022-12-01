from aoc import get_input

data = get_input(2).splitlines()

def main(data: list) -> int:
    for line in data:   # Iterate Over Each Line in Data
        print(line)

    return None

if __name__ == '__main__':
    # Get Input Data
    data = get_input(1).splitlines()
    
    # Print Answer
    print(main(data))