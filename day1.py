with open(r'day1data.txt') as f:
    data = f.read()

data = data.split('\n\n')
for i in range(len(data)):
    data[i] = data[i].split()


max_elf_end = []
max_calories_end = []
for i in range(3):
    max_calories = 0
    max_elf = 0
    for elf,calories in enumerate(data):
        if (elf + 1) in max_elf_end:
            continue
        calorie_count = 0
        for food in calories:
            calorie_count += int(food)
        if calorie_count > max_calories:
            max_calories = calorie_count
            max_elf = elf + 1
    max_elf_end.append(max_elf)
    max_calories_end.append(max_calories)
    

print(max_elf_end,max_calories_end,sum(max_calories_end))
