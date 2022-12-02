from aoc import get_input

dictionary = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'} # Dictionary Mapping Input Symbols to RPS Throw

# Dictionaries Mapping Symobls to Scores
result_score = {'Z': 6, 'X': 3, 'Y': 0} # Score for Winning, Tying, or Losing
throw_score = {'R': 1, 'P': 2, 'S': 3}  # Score for RPS Throw

# Determine Throw Based on Opponent's Throw and Desired Outcome
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
    score = 0   # Total Score for All Games
    
    for line in data:   # Iterate Over Each Line in Data
        # Split Player Throws
        line = line.split(' ')
        
        opponent = line[0]
        self = line[1]
        
        score += result_score[self] # Add Result Score
        
        self_throw = throw(dictionary[opponent], self)  # Determine Throw
        
        score += throw_score[self_throw]    # Add Throw Score

    return score

if __name__ == '__main__':
    # Get Input Data
    data = get_input(2).splitlines()
    
    # Print Answer
    print(main(data))