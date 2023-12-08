import time

In = open("d8input.txt").read()
In = In.split("\n")

def conv(a):
    return 26*26*(ord(a[0])-64)+26*(ord(a[1])-64)+(ord(a[2])-64)

def convback(a):
    s  = ''
    while a != 0:
        s = chr(a % 26+64) + s
        a = a // 26
    return s


instr, paths = In[0], In[2:len(In)-1]

go = [0]*20000
tracking = []
for path in paths:
    first = conv(path[0:3])
    if first % 26 == 1:
        tracking.append(first)
    go[first] = [conv(path[7:10]), conv(path[12:15])]

curr = conv("AAA")
steps = 0
i = 0

while curr != conv("ZZZ"):
    ch = instr[i]
    if ch == "L":
        curr = go[curr][0]
    elif ch == "R":
        curr = go[curr][1]
    steps += 1
    i = (i+1)%len(instr)
print(steps)

def allz(ta):
    for item in ta:
        if item % 26 != 0:
            return False
    return True


steps = 0
i = 0
    
while not allz(tracking):
    ch = instr[i]
    for j, item in enumerate(tracking):
        if ch == "L":
            tracking[j] = go[tracking[j]][0]
        elif ch == "R":
            tracking[j] = go[tracking[j]][1]
    steps += 1
    i = (i+1)%len(instr)
print(steps)
    
