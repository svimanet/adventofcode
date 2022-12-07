
data = ''
with open('6.txt','r') as f:
    data = f.read()
    data.strip()

def func(n):
    for i,char in enumerate(data):

        sliced = data[i:i+n]
        gotonext = False
        tmp = ''
        for x in sliced:
            if x not in tmp: tmp += x
            else:
                gotonext = True
                break

        if gotonext: continue
        print('\n\nEnd at \'{}\' - {}'.format(sliced, (i+n)))
        break

func(4)  # Part1
func(14) # Part2

