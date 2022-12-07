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
            if commandType(line) == 'ls':
                j = copy.copy(index) 
                try:
                    while lineType(data[j + 1]) != 'command':
                        if lineType(data[j + 1]) == 'directory':
                            print('hi')
                        else:
                            directories.setdefault(currentDirectory[-1],0)
                            for i in range(len(currentDirectory)):
                                directories[currentDirectory[i]] += fileSize(data[j + 1])
                        j += 1
                except:
                    pass

    sum = 0
    for size in directories.values():
        if size <= 100_000:
            sum += size
    print(sum)
    print(directories)
    print(currentDirectory)



def main():
    response = int(input('1 for example, 2 for actual: '))
    if response == 1:
        file = r'day7ex.txt'
    else:
        file = r'day7data.txt'
    with open(file) as f:
        data = f.read().split('\n')

    part1(data)

if __name__ == "__main__":
    main()
