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
        number_of_stacks = 3
    else:
        file = r'day5data.txt'
        number_of_stacks = 9

    with open(file) as f:
        data = f.read()
    data = data.split('\n\n')
    structure,instructions = data

    instructionRegex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    instructions = instructionRegex.findall(instructions)

    structureRegex = re.compile(r'(\s{3}|\[\w\])\s')
    structure = structureRegex.findall(structure)

    stacks = []

    for i in range(number_of_stacks):
        stacks.append([structure[i + (j * 3)] for j in range(number_of_stacks)][::-1])
        while stacks[i][-1] == '   ':
            del stacks[i][-1]
    print(stacks)

    stacks2 = copy.deepcopy(stacks)

    part1(stacks,instructions)
    part2(stacks2,instructions)

main()