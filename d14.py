In = open("d14input.txt").read().strip()
In = In.split("\n")
G = [[c for c in row] for row in In]
G2 = [[c for c in row] for row in In]

def p(a):
    for r in a:
        for c in r:
            print(c, end="")
        print()
    print()

def rot(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def tilt(ng):
    while True:
        swaps = False
        for r, row in enumerate(ng):
            for c, ch in enumerate(row):
                if ch == "O":
                    if r > 0:
                        if ng[r-1][c] == ".":
                            ng[r-1][c] = "O"
                            ng[r][c] = "."
                            swaps = True
        if not swaps:
            return ng

G = tilt(G) 
total = 0
for r, row in enumerate(G):
    for c, ch in enumerate(row):
        if ch == "O":
            total = total + (len(G)-r)
print(total)


D = {} #dictionary to detect cycle (key is grid, data is loop number)
i = 0
while i < 1000000000:

    for x in range(4):
        G2 = tilt(G2)
        G2 = rot(G2)

    Gh = tuple(tuple(row) for row in G2)
    if Gh in D:
        if i <900000000:
            #skip forward to close to a billion
            ltg = 1000000000 - i
            cyclelength = i - D[Gh]
            skip = ltg//(cyclelength)
            i += (cyclelength*skip)
    else:
        D[Gh] = i
    i = i + 1
#work out the score
total = 0
for r, row in enumerate(G2):
    for c, ch in enumerate(row):
        if ch == "O":
            total = total + (len(G2)-r)
print(total)
