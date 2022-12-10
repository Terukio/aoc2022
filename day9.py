class Rope:
    def __init__(self,part):
        self.knots = [Knot() for i in range(part)]
        self.visited_locations = set()
    
    def move(self,instruction):
        instruction = instruction.split()
        direction,amount = instruction
        amount = int(amount)
        head = self.knots[0]
        for _ in range(amount):
            if direction == 'U':
                head.y += 1
            elif direction == 'D':
                head.y -= 1
            elif direction == 'L':
                head.x -= 1
            else:
                head.x += 1
            for parent,knot in enumerate(self.knots[1:]):
                if not knot.adjacent(self.knots[parent]):
                    knot.move(self.knots[parent])
            self.visited_locations.add((self.knots[-1].x,self.knots[-1].y))

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def adjacent(self,parent):
        if abs(parent.x - self.x) > 1 or abs(parent.y - self.y) > 1:
            return False
        else:
            return True
    
    def move(self,parent):
        if parent.x - self.x > 1:
            self.x += 1
            self.y = parent.y
        if parent.x - self.x < -1:
            self.x -= 1
            self.y = parent.y
        if parent.y - self.y > 1:
            self.y += 1
            self.x = parent.x
        if parent.y - self.y < -1:
            self.y -= 1
            self.x = parent.x


def part1(data):
    rope = Rope(2)
    for instruction in data:
        rope.move(instruction)
    print(len(rope.visited_locations))

def part2(data):
    rope = Rope(10)
    for instruction in data:
        rope.move(instruction)
    print(len(rope.visited_locations))


def main():
    testing = False
    if testing:
        file = r'day9ex.txt'
    else:
        file = r'day9data.txt'
    with open(file) as f:
        data = f.read()
    data = data.split('\n')
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()