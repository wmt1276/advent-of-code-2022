from aoc import get_input

dictionary = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
score_dict = {'Z': 6, 'Y': 3, 'X': 0}
throw_score = {'R': 1, 'P': 2, 'S': 3}

def throw(opponent, self):
    if self == 'Y':
        return opponent
    else:
        if opponent == 'R':
            if self == 'X':
                return 'S'
            elif self == 'Z':
                return 'P'
        elif opponent == 'P':
            if self == 'X':
                return 'R'
            elif self == 'Z':
                return 'S'
        elif opponent == 'S':
            if self == 'X':
                return 'P'
            elif self == 'Z':
                return 'R'

def main(data: list) -> int:
    score = 0
    
    for line in data:   # Iterate Over Each Line in Data
        line = line.split(' ')
        score += score_dict[line[1]]
        
        thro = throw(dictionary[line[0]], line[1])
        
        score += throw_score[thro]

    return score

if __name__ == '__main__':
    # Get Input Data
    data = get_input(2).splitlines()
    
    # Print Answer
    print(main(data))