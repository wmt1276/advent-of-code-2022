from aoc import get_input

dictionary = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'} # Dictionary Mapping Input Symbols to RPS Throw

# Dictionaries Mapping Symobls to Scores
result_score = {'W': 6, 'T': 3, 'L': 0} # Score for Winning, Tying, or Losing
throw_score = {'R': 1, 'P': 2, 'S': 3}  # Score for RPS Throw

# Determine Winner of RPS Game
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

def main(data: list) -> int:
    score = 0   # Total Score for All Games
    
    for line in data:   # Iterate Over Each Line in Data
        # Split Player Throws
        line = line.split(' ')
        
        opponent = line[0]
        self = line[1]
        
        outcome = win(dictionary[opponent], dictionary[self]) # Determine Outcome of RPS Game
        
        # Tabulate Score of Match
        score += result_score[outcome]  # Add Result Score
        score += throw_score[dictionary[self]]  # Add Throw Score

    return score

if __name__ == '__main__':
    # Get Input Data
    data = get_input(2).splitlines()
    
    # Print Answer
    print(main(data))