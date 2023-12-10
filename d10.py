In = open("d10input.txt").read()
In = In.split("\n")[0:-1]

In2 = In.copy() #keeps track of what cells are on the loop - a cell is changed to an X

def cc(pos):
    return In[pos[0]][pos[1]]

i = 0
curr = [0, 0]
prev = curr

#find the start cell
for r, line in enumerate(In):
    for c, ch in enumerate(line):
        if ch == "S":
            curr = [r, c]

prev = curr
curr = [curr[0]-1, curr[1]]  #this is hardcoding which direction to start in and will not work if the loop can't start up
i = i + 1
In2[curr[0]] = original_string = In2[curr[0]][:curr[1]] + "X" + In2[curr[0]][curr[1] + 1:]


while cc(curr) != "S":
    if cc(curr) == "-":
        if prev[1] < curr[1]:
            prev = curr.copy()
            curr[1] = curr[1]+1
        else:
            prev = curr.copy()
            curr[1] = curr[1]-1
    elif cc(curr) == "|":
        if prev[0] < curr[0]:
            prev = curr.copy()
            curr[0] = curr[0] + 1
        else:
            prev = curr.copy()
            curr[0] = curr[0] -1
    elif cc(curr) == "F":
        if prev[0]>curr[0]:
            prev = curr.copy()
            curr[1] = curr[1]+1
        else:
            prev = curr.copy()
            curr[0] += 1
    elif cc(curr) == "L":
        if prev[0] < curr[0]:
            prev = curr.copy()
            curr[1] += 1
        else:
            prev = curr.copy()
            curr[0] -= 1
    elif cc(curr) == "J":
        if prev[1] < curr[1]:
            prev = curr.copy()
            curr[0] -= 1
        else:
            prev = curr.copy()
            curr[1] -= 1
    elif cc(curr) == "7":
        if prev[1] < curr[1]:
            prev = curr.copy()
            curr[0] += 1
        else:
            prev = curr.copy()
            curr[1] -= 1
    In2[curr[0]] = original_string = In2[curr[0]][:curr[1]] + "X" + In2[curr[0]][curr[1] + 1:] #update the grid with what is on the loop
    i += 1
print(i//2)

insides = 0
for r, line in enumerate(In):
    for c, ch in enumerate(line):
        if In2[r][c] != "X":
            row = r
            col = c
            crossings = 0
            while row >=0 and crossings >= 0:
                if In2[row][col] == "X" and In[row][col] != "L" and In[row][col] != "7":
                    crossings += 1
                row -= 1
                col -= 1
            if crossings % 2 == 1:
                insides += 1
print(insides)
