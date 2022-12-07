data = []
with open('7.txt', 'r') as f:
    data = f.readlines()

dirs = {}

currentDir = ''

breadcrumbs = ['/']

treeLvl = 0

for line in data:
    line = line.strip()

    

    if '$ cd' in line:
        if '/' in line: continue # Ignore first root cd

        # CD down a level, add current dir to path
        if '..' not in line:
            treeLvl += 1
            dirr = line.split(' ')[2]
            breadcrumbs.append(dirr)

        # If CD back, pop last dir in path
        elif '..' in line:
            treeLvl -= 1
            breadcrumbs.pop()

    currentPath = ['/{}'.format(x) for x in breadcrumbs]


    filename = ''
    size = 0
    nums = '0123456789'
    for num in nums:
        if num in line: # If line contains num, it's a filesize
            strnum = line.split(' ')[0]
            filename = line.split(' ')[1]
            size = int(strnum)
            break

    try:
        dirs[currentPath] += size
    except:
        dirs[currentPath] = size


total = 0
for k,v in dirs.items():
    if v > 100000: continue
    total += v


print(dirs)
print(total)
