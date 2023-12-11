In = open("d11input.txt").read()[:-1].split("\n")

mr = []
mc = []
gals = []

#Find the rows without galaxies
i = 0
while i < len(In):
    if not "#" in In[i]:
        mr.append(i)
    i = i + 1

#find the columns without galaxies (gross)
j = 0
while j < len(In[0]):
    In2 = []
    isEmpty = True
    for k in range(len(In)):
        if In[k][j] == "#":
            isEmpty = False
    if isEmpty:
        mc.append(j)
        j = j+1
    j = j + 1

#build a list of a coords of galaxies   
for i, line in enumerate(In):
    for j, ch in enumerate(line):
        if ch == "#":
            rt = i
            ct = j
            for r in mr:
                if i > r:
                    rt += 999999
            for c in mc:
                if j > c:
                    ct += 999999
            
            gals.append((rt,ct))

#for each pair of galaxies - calc their distance and add to total
i = 0
total = 0
while i < len(gals):
    j = i+1
    while j < len(gals):
        dist = abs(gals[i][0]-gals[j][0])+abs(gals[i][1]-gals[j][1])
        total += dist
        j = j + 1
    i = i + 1
print(total)
