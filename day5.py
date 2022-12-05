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
    else:
        file = r'day5data.txt'

    with open(file) as f:
        data = f.read()
    data = data.split('\n\n')
    structure,instructions = data

    instructionRegex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    instructions = instructionRegex.findall(instructions)

    structure = structure.split('\n')
    
    newStructure = []
    for j in range(len(structure)):
        items = []
        for i in range(len(structure[j])):
            if (i + 1) % 4 == 0:
                continue
            elif structure[j][i] == '[':
                continue
            elif structure[j][i] == ']':
                continue
            elif structure[j][i] != ' ':
                items.append(structure[j][i])
            elif (i + 1) % 2 == 0:
                items.append(' ')
        newStructure.append(items)

    stacks = [[] for _ in range(len(newStructure[-1]))]

    for info in newStructure[::-1]:
        for i in range(len(info)):
            if info[i] != ' ':
                stacks[i].append(info[i])

    for i in range(len(stacks)):
        del stacks[i][0]

    stacks2 = copy.deepcopy(stacks)

    part1(stacks,instructions)
    part2(stacks2,instructions)

main()