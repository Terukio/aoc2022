def priority(letter):
    letters = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letters.index(letter)

def compartmentalize(rucksack):
    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2:]
    return compartment1,compartment2

def shared_item(rucksack):
    compartment1,compartment2 = compartmentalize(rucksack)
    shared_items = ''
    for item in compartment1:
        if item in compartment2:
            shared_items += item
            break
    return shared_items

def create_groups(data):
    groups = []
    current_group = []
    for rucksack in data:
        current_group.append(rucksack)
        if len(current_group) == 3:
            groups.append(current_group)
            current_group = []
    return groups

def group_shared_item(group):
    elf1,elf2,elf3 = group
    elf1,elf2,elf3 = set(elf1),set(elf2),set(elf3)
    overlapping_items = ''.join(elf1.intersection(elf2).intersection(elf3))
    return overlapping_items

def part1(data):
    shared_items = ''
    sum_of_priorities = 0
    for rucksack in data:
        shared_items += shared_item(rucksack)
    for item in shared_items:
        sum_of_priorities += priority(item)
    print(sum_of_priorities)

def part2(data):
    groups = create_groups(data)
    lettered_groups = ''
    sum_of_priorities = 0
    for group in groups:
        lettered_groups += group_shared_item(group)
    for letter in lettered_groups:
        sum_of_priorities += priority(letter)
    print(sum_of_priorities)
        
            
def main():
    response = int(input('Type 1 for example, 2 for actual: '))
    if response == 1:
        with open(r'day3ex.txt') as f:
            data = f.read()
    else:
        with open(r'day3data.txt') as f:
            data = f.read()
    data = data.split()
    part1(data)
    part2(data)

main()