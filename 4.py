
data = []
with open('4.txt', 'r') as f:
    data = f.readlines()


def get_range(inp, diff, end):
    rng = []
    for x in range(diff):
        rng.append(int(inp)+x)
    rng.append(int(end))
    return rng


def get_overlap(a, b):
    inb = []
    for x in a:
        if x in b:
            inb.append(True)
        else: inb.append(False)
    return inb


overlaps = 0
for row in data:
    row = row.strip().split(',')
    a = row[0].split('-')
    b = row[1].split('-')

    diff_a = int(a[1]) - int(a[0])
    diff_b = int(b[1]) - int(b[0])

    range_a = get_range(a[0], diff_a, a[1])
    range_b = get_range(b[0], diff_b, b[1])

    a_overlap = get_overlap(range_a, range_b)
    a_full = all(x is True for x in a_overlap)

    b_overlap = get_overlap(range_b, range_a)
    b_full = all(x is True for x in b_overlap)

    if b_full or a_full: overlaps += 1
    

print('Answer 1:', overlaps)


overlaps = 0
for row in data:
    row = row.strip().split(',')
    a = row[0].split('-')
    b = row[1].split('-')

    diff_a = int(a[1]) - int(a[0])
    diff_b = int(b[1]) - int(b[0])

    range_a = get_range(a[0], diff_a, a[1])
    range_b = get_range(b[0], diff_b, b[1])

    a_overlap = get_overlap(range_a, range_b)
    b_overlap = get_overlap(range_b, range_a)

    any_a = any(a_overlap)
    any_b = any(b_overlap)

    if any_a or any_b: overlaps += 1


print('Answer 2:', overlaps)
