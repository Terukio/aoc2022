def sectionAssignment(elf):
    elf = elf.split('-')
    return set([i for i in range(int(elf[0]),int(elf[1])+1)])

def part1(data):
    count = 0
    for pair in data:
        elf_1_assignment, elf_2_assignment = sectionAssignment(pair[0]),sectionAssignment(pair[1])
        if (elf_1_assignment.issubset(elf_2_assignment)) or (elf_2_assignment.issubset(elf_1_assignment)):
            count += 1
    print(count)

def part2(data):
    count = 0
    for pair in data:
        elf_1_assignment, elf_2_assignment = sectionAssignment(pair[0]),sectionAssignment(pair[1])
        if len(elf_1_assignment.intersection(elf_2_assignment)) != 0:
            count +=1
    print(count)

def main():
    response = int(input('Type 1 for example, 2 for actual: '))
    if response == 1:
        file = r'day4ex.txt'
    else:
        file = r'day4data.txt'
    with open(file) as f:
        data = f.read()
    data = data.split()
    for i in range(len(data)):
        data[i] = data[i].split(',')

    part1(data)
    part2(data)

main()