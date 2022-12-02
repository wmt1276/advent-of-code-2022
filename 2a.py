from aoc import get_input

dictionary = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
score_dict = {'W': 6, 'T': 3, 'L': 0}
throw_score = {'R': 1, 'P': 2, 'S': 3}

def main(data: list) -> int:
    score = 0
    
    for line in data:   # Iterate Over Each Line in Data
        line = line.split(' ')
        outcome = win(dictionary[line[0]], dictionary[line[1]])
        score += score_dict[outcome]
        score += throw_score[dictionary[line[1]]]

    return score

def win(opponent, self):
    if opponent == 'R':
        if self == 'R':
            return 'T'
        elif self == 'P':
            return 'W'
        elif self == 'S':
            return 'L'
    elif opponent == 'P':
        if self == 'R':
            return 'L'
        elif self == 'P':
            return 'T'
        elif self == 'S':
            return 'W'
    elif opponent == 'S':
        if self == 'R':
            return 'W'
        elif self == 'P':
            return 'L'
        elif self == 'S':
            return 'T'

if __name__ == '__main__':
    # Get Input Data
    data = get_input(2).splitlines()
    
    # Print Answer
    print(main(data))