class Tree:
    def __init__(self,x,y,height):
        self.x = x
        self.y = y
        self.height = height
        self.visible_top = True
        self.visible_bottom = True
        self.visible_left = True
        self.visible_right = True
        self.visible = False
        self.left_count = 0
        self.right_count = 0
        self.top_count = 0
        self.bottom_count = 0
        self.scenic_score = 1

    def make_visible(self):
        self.visible = True

def part1(data):
    position_x,position_y = (0,0)
    trees = []
    forest_width,forest_height = len(data.split()[0]),len(data.split())
    for char in data:
        if char != '\n':
            trees.append(Tree(position_x,position_y,int(char)))
            position_x += 1
        else:
            position_x = 0
            position_y += 1
    for tree in trees:
        if tree.x == 0 or tree.x == forest_width or tree.y == 0 or tree.y == forest_height:
            tree.make_visible()
        else:
            for other_tree in trees:
                if tree.y == other_tree.y:
                    if other_tree.x < tree.x and other_tree.height >= tree.height and tree.visible_left:
                        tree.visible_left = False
                    elif other_tree.x > tree.x and other_tree.height >= tree.height and tree.visible_right:
                        tree.visible_right = False
                elif tree.x == other_tree.x:
                    if other_tree.y < tree.y and other_tree.height >= tree.height and tree.visible_top:
                        tree.visible_top = False
                    elif other_tree.y > tree.y and other_tree.height >= tree.height and tree.visible_bottom:
                        tree.visible_bottom = False
        if tree.visible_left or tree.visible_right or tree.visible_top or tree.visible_bottom:
            tree.make_visible()
    count = 0
    for tree in trees:
        if tree.visible:
            count += 1
    print(count)

def part2(data):
    position_x,position_y = (0,0)
    trees = []
    forest_width,forest_height = len(data.split()[0]),len(data.split())
    for char in data:
        if char != '\n':
            trees.append(Tree(position_x,position_y,int(char)))
            position_x += 1
        else:
            position_x = 0
            position_y += 1
    for tree in trees:
        if tree.x == 0 or tree.x == forest_width or tree.y == 0 or tree.y == forest_height:
            tree.scenic_score = 0
        else:
            trees_to_the_right = sorted([other_tree for other_tree in trees if (other_tree.y == tree.y and other_tree.x > tree.x)],key=lambda a: a.x)
            for other_tree in trees_to_the_right:
                if other_tree.height >= tree.height:
                    tree.right_count += 1
                    break
                else:
                    tree.right_count += 1
            trees_to_the_left = sorted([other_tree for other_tree in trees if (other_tree.y == tree.y and other_tree.x < tree.x)],key=lambda a: a.x, reverse=True)
            for other_tree in trees_to_the_left:
                if other_tree.height >= tree.height:
                    tree.left_count += 1
                    break
                else:
                    tree.left_count += 1
            trees_above = sorted([other_tree for other_tree in trees if (other_tree.x == tree.x and other_tree.y < tree.y)],key=lambda a: a.y, reverse=True)
            for other_tree in trees_above:
                if other_tree.height >= tree.height:
                    tree.top_count += 1
                    break
                else:
                    tree.top_count += 1
            trees_below = sorted([other_tree for other_tree in trees if (other_tree.x == tree.x and other_tree.y > tree.y)],key=lambda a: a.y)
            for other_tree in trees_below:
                if other_tree.height >= tree.height:
                    tree.bottom_count += 1
                    break
                else:
                    tree.bottom_count += 1
            

                

    scenic_counts = []
    for tree in trees:
        tree.scenic_score *= (tree.bottom_count * tree.top_count * tree.left_count * tree.right_count)
        scenic_counts.append(tree.scenic_score)
    print(max(scenic_counts))
                
def main():
    testing = False
    if testing:
        file = r'day8ex.txt'
    else:
        file = r'day8data.txt'
    with open(file) as f:
        data = f.read()
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
    