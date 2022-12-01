from aoc import get_input

def main(data: list) -> int:
    for line in data:   # Iterate Over Each Line in Data
        print(line)

    return None

if __name__ == '__main__':
    # Get Input Data
    data = get_input(2).splitlines()
    
    # Print Answer
    print(main(data))