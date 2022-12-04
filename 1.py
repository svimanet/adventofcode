
rawdata = ''
data = []
tmp = 0

with open('1.txt') as f: rawdata = f.readlines()

for line in rawdata:
    x = line.strip()
    if len(x) > 0: 
        tmp += int(x)
    else: 
        data.append(tmp)
        tmp = 0

data.sort()
a1 = data[-1]
print('Answer 1:', a1)

top3 = data[-3:]
a2 = 0
for x in top3: a2 += x
print('Answer 2:', a2)
