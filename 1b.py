from aoc import get_input

data = get_input(1).splitlines()

def main(data: list) -> int:
    elf_totals = [] # Store Total Calories for Each Elf
    
    elf = 0 # Store Total Calories of Current Elf (Initialized to 0)
    for line in data:   # Iterate Over Each Line in Data
        if line == "":  # End of Elf's Calories -> Add to elf_totals and Reset elf
            elf_totals.append(elf)
            
            elf = 0
            
        else:   # Add Calories to Current Elf
            elf += int(line)
            
    elf_totals = sorted(elf_totals) # Sort elf_totals
    elf_totals.reverse()    # Reverse elf_totals
    
    return sum(elf_totals[:3])  # Return Sum of Top 3

if __name__ == '__main__':
    # Get Input Data
    data = get_input(1).splitlines()
    
    # Print Answer
    print(main(data))