In = open("d18input.txt").read().strip()
In = In.split("\n")
x=0
y=0
x2 = 0
y2 = 0
corners = []
c2 = []
perim = 0
p2 = 0
for line in In:

    d, dist, colour = line.split()
    colour = colour[2:-1]
    
    d2 = {0: "R", 1:"D", 2:"L", 3:"U"}[int(colour[5])]
    dist = int(dist)
    dist2 = int(colour[0:-1], 16)
    
    perim = perim+dist
    p2 = p2 + dist2
    
    if d == "U":
        y=y+dist
    elif d == "D":
        y = (y-dist)
    elif d == "L":
        x = (x - dist)
    elif d == "R":
        x = x + dist
    corners.append((x, y))

    if d2 == "U":
        y2=y2+dist2
    elif d2 == "D":
        y2 = (y2-dist2)
    elif d2 == "L":
        x2 = (x2 - dist2)
    elif d2 == "R":
        x2 = x2 + dist2
    c2.append((x2, y2))

#corners = [(1,0),(7,0),(7,3),(5,3), (5,4), (7,4),(7,10), (0,10),(0,7),(2,7),(2,5),(0,5),(0,2),(1,2)]


sum1 = 0
sum2 = 0
rcorners = corners[::-1]
for i in range(len(rcorners)):
    sum1 = sum1 + (rcorners[i][0] * rcorners[(i+1)%len(rcorners)][1])
    sum2 = sum2 + (rcorners[i][1] * rcorners[(i+1)%len(rcorners)][0])
A = abs(sum1 - sum2) / 2
A = A + perim / 2 + 1
print(A)

sum1 = 0
sum2 = 0
rcorners = c2[::-1]
for i in range(len(rcorners)):
    sum1 = sum1 + (rcorners[i][0] * rcorners[(i+1)%len(rcorners)][1])
    sum2 = sum2 + (rcorners[i][1] * rcorners[(i+1)%len(rcorners)][0])
A = abs(sum1 - sum2) / 2
A = A + p2 / 2 + 1
print(A)
