import re,copy

def part1(structure,instructions):
    for instruction in instructions:
        items,currentLocation,newLocation = instruction
        items,currentLocation,newLocation = int(items),int(currentLocation),int(newLocation)
        for _ in range(items):
            structure[newLocation - 1].append(structure[currentLocation - 1][-1])
            structure[currentLocation - 1] = structure[currentLocation - 1][:-1]
    for stack in structure:
        print(stack[-1],end='')
    print()
    
def part2(structure,instructions):
    for instruction in instructions:
        items,currentLocation,newLocation = instruction
        items,currentLocation,newLocation = int(items),int(currentLocation),int(newLocation)
        structure[newLocation - 1] += structure[currentLocation - 1][-items:]
        for _ in range(items):
            structure[currentLocation - 1] = structure[currentLocation - 1][:-1]
    for stack in structure:
        print(stack[-1],end='')
    print()
    
def main():
    response = int(input('1 for example, 2 for actual: '))
    if response == 1:
        file = r'day5ex.txt'
        stack1 = ['Z','N']
        stack2 = ['M','C','D']
        stack3 = ['P']
        structure = [stack1,stack2,stack3]
        structure2 = copy.deepcopy(structure)
    else:
        file = r'day5data.txt'
        stack1 = ['F','T','C','L','R','P','G','Q']
        stack2 = ['N','Q','H','W','R','F','S','J']
        stack3 = ['F','B','H','W','P','M','Q']
        stack4 = ['V','S','T','D','F']
        stack5 = ['Q','L','D','W','V','F','Z']
        stack6 = ['Z','C','L','S']
        stack7 = ['Z','B','M','V','D','F']
        stack8 = ['T','J','B']
        stack9 = ['Q','N','B','G','L','S','P','H']
        structure = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
        structure2 = copy.deepcopy(structure)

    with open(file) as f:
        data = f.read()
    data = data.split('\n\n')
    _,instructions = data
    instructionRegex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    instructions = instructionRegex.findall(instructions)
    
    part1(structure,instructions)
    part2(structure2,instructions)

main()