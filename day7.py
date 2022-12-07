import copy

def commandType(command):
    if '$ cd' in command:
        return 'cd'
    elif '$ ls' in command:
        return 'ls'

def lineType(line):
    if line[0] == '$':
        return 'command'
    elif line[0:3] == 'dir':
        return 'directory'
    else:
        return 'file'

def cd(command):
    if command[5:7] == '..':
        return 'out'
    if command[5] == '/':
        return '/'
    else:
        return command[5:]

def fileSize(file):
    filesize = ''
    for char in file:
        if char != ' ':
            filesize += char
        else:
            return int(filesize)

def part1(data):
    directories = {'/' : 0}
    currentDirectory = ['/']    
    for index,line in enumerate(data):
        if lineType(line) == 'command':
            if commandType(line) == 'cd':
                if cd(line) == 'out':
                    del currentDirectory[-1]
                elif cd(line) == '/':
                    currentDirectory = ['/']
                else:
                    currentDirectory.append(cd(line))
        elif lineType(line) == 'directory':
            cur = copy.copy(currentDirectory)
            cur.append(line[4:])
            directoryName = '_'.join(cur)
            if directoryName not in directories.keys():
                directories.setdefault(directoryName,0)
        else:
            size = fileSize(line)
            for i in range(len(currentDirectory)):
                directories['_'.join(currentDirectory[:i+1])] += size

    sum = 0
    for size in directories.values():
        if size <= 100_000:
            sum += size

    return sum,directories

def part2(directories):
    used_space = directories['/']
    total_space = 70_000_000
    needed_space = 30_000_000
    empty_space = total_space - used_space
    possibilities = []
    for directory,size in directories.items():
        if empty_space + size >= needed_space:
            possibilities.append(size)
    print(min(possibilities))


def main():
    response = int(input('1 for example, 2 for actual: '))
    if response == 1:
        file = r'day7ex.txt'
    else:
        file = r'day7data.txt'
    with open(file) as f:
        data = f.read().split('\n')

    print(part1(data)[0])
    part2(part1(data)[1])
 

if __name__ == "__main__":
    main()
