
alpha = 'abcdefghijklmnopqrstuvwxyz'
prios = {}
for k,char in enumerate(alpha):
    prios[char] = k+1
    prios[char.upper()] = k+26+1


data = []
with open('3.txt', 'r') as f:
    data = f.readlines()


scores = []
for k,v in enumerate(data):
    v = v.strip()
    leng = len(v)
    half = round(leng/2)
    a = v[0:half]
    b = v[half:]

    counted = []
    for char in a:
        if char in b and char not in counted:
            scores.append(prios[char])
            counted.append(char)


print('Answer 1:', sum(scores))


count = 0
group = []
groups = []
for v in data:
    v = v.strip()
    count += 1
    group.append(v)
    if count == 3: 
        count = 0
        groups.append(group)
        group = []

scores = []
for group in groups:
    counted = []
    row1 = group[0]
    row2 = group[1]
    row3 = group[2]

    in2 = []
    in3 = []
    common = []

    for char in row1:
        if char in row2 and char in row3 and char not in common: # ew
            common.append(char)
            scores.append(prios[char])


print('Answer 2:', sum(scores)) 


        
