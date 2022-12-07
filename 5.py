# Cols:
# [N]     [Q]         [N]            
# [R]     [F] [Q]     [G] [M]        
# [J]     [Z] [T]     [R] [H] [J]    
# [T] [H] [G] [R]     [B] [N] [T]    
# [Z] [J] [J] [G] [F] [Z] [S] [M]    
# [B] [N] [N] [N] [Q] [W] [L] [Q] [S]
# [D] [S] [R] [V] [T] [C] [C] [N] [G]
# [F] [R] [C] [F] [L] [Q] [F] [D] [P]
#  1   2   3   4   5   6   7   8   9 

# Data:
# move 3 (3 stk) from 9 (column) to 4 (column)

import pprint
pp = pprint.PrettyPrinter(indent=4)

data = []
with open('5.txt','r') as f:
    for x in f.readlines():
        data.append(x.strip())

# Create list of column values
tmp = []
with open('5cols.txt','r') as f:
    for line in f.readlines():
        tmp.append(line)
tmp.reverse()


# Init lists to append in dic
cols = {}
for x in range(1,10):
    cols[x] = []

# Make columns dynamically
positions = [1, 5, 9, 13, 17, 21, 25, 29, 33]
alpha = 'abcdefghijklmnopqrstuvwxyz'
for k,line in enumerate(tmp):
    if '1' in line: continue  # Only legend contains nummericals

    for i,char in enumerate(line):
        if char.lower() in alpha:
            pos = positions.index(i) + 1
            cols[pos].append(char)

import copy
cols2 = copy.deepcopy(cols) # Make copy for part 2



# resolve steps part 1
for line in data:
    line = line.split(' ')
    n = int(line[1])  # Quantity
    fm = int(line[3]) # From
    to = int(line[5]) # To

    fm_col = cols[fm]
    to_col = cols[to]

    for x in range(n):
        to_move = fm_col.pop()
        to_col.append(to_move)

answer1 = ''
for col in cols.values():
    answer1 += col[-1]

print('Answer1:', answer1)



# resolve steps part 2
for line in data:
    line = line.split(' ')
    n = int(line[1])  # Quantity
    fm = int(line[3]) # From
    to = int(line[5]) # To

    fm_col = cols2[fm]
    to_col = cols2[to]

    to_move = fm_col[-n:]

    del fm_col[-n:]
    to_col.extend(to_move)

answer2 = ''
for col in cols2.values():
    answer2 += col[-1]

print('Answer2:', answer2)



