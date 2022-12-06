def part1(data):
    for i in range(len(data) - 4):
        letters = set(data[i:i + 4])
        if len(letters) == 4:
            print(i + 4)
            break

def part2(data):
    for i in range(len(data) - 14):
        letters = set(data[i:i + 14])
        if len(letters) == 14:
            print(i + 14)
            break

def main():
    response = int(input('1 for example, 2 for actual: '))
    if response == 1:
        file = r'day6ex.txt'
    else:
        file = r'day6data.txt'

    with open(file) as f:
        data = f.read()

    part1(data)
    part2(data)

if __name__ == '__main__':
    main()