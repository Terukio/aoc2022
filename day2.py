with open(r'day2data.txt') as f:
    data = f.read()
data = data.split('\n')

def part1(data):

    total_score = 0

    tie_dict = {'X':'A',
                'Y':'B',
                'Z':'C'}

    for game in data:
        if game[0] == tie_dict[game[-1]]:
            total_score += 3
        elif (game[0] == 'A' and game[-1] == 'Z') or (game[0] == 'B' and game[-1] == 'X') or (game[0] == 'C' and game[-1] == 'Y'):
            total_score += 0
        else:
            total_score += 6
        if game[-1] == 'X':
            total_score += 1
        elif game[-1] == 'Y':
            total_score += 2
        else:
            total_score += 3

    print(total_score)

def part2(data):

    map = {'A X' : 3,
           'A Y' : 4,
           'A Z' : 8,
           'B X' : 1,
           'B Y' : 5,
           'B Z' : 9,
           'C X' : 2,
           'C Y' : 6,
           'C Z' : 7,}
    
    total_score = 0

    for game in data:
        total_score += map[game]
    
    print(total_score)

part1(data)
part2(data)