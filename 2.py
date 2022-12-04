
a = 'a' # rock
b = 'b' # paper
c = 'c' # sci

x = 'x' # rock
y = 'y' # paper
z = 'z' # sci

wins = [(a,y), (b,z), (c,x)]
draw = [(a,x), (b,y), (c,z)]

scores = []

data = []

with open('2.txt', 'r') as f:
    for line in f.readlines():
        strp = line.strip()
        if len(strp) > 0: data.append(strp)


for tupl in data:
    score = 0
    xx = tupl[0].lower()
    yy = tupl[2].lower()
    tup = (xx, yy)

    if tup in wins: score += 6
    elif tup in draw: score += 3

    if yy == 'x': score += 1
    elif yy == 'y': score += 2
    elif yy == 'z': score += 3
    

    scores.append(score)


print('Answer 1:', str(sum(scores)))

scores2 = []

for tupl in data:
    score = 0
    xx = tupl[0].lower()  # opponent pick
    yy = tupl[2].lower()  # resolution
    tup = (xx, yy)
    our = '' # our pick

    if yy == y:  # must draw
        score += 3
        if xx == a: our = x
        if xx == b: our = y
        if xx == c: our = z

    if yy == x:  # must lose
        if xx == a: our = z # rock v sci
        if xx == b: our = x # paper v rock
        if xx == c: our = y # sci v paper

    if yy == z:  # must win
        score += 6
        if xx == a: our = y # rock v paper
        if xx == b: our = z # paper v sci
        if xx == c: our = x # sci v rock

    if our == x: score += 1
    if our == y: score += 2
    if our == z: score += 3

    scores2.append(score)


print('Answer 2:', str(sum(scores2)))








