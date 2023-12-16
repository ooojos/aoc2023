In = open("d16input.txt").read().strip()
G = [[c for c in row] for row in In.split("\n")]

def move(c, d):
    return [sum(x) for x in zip(c, d)]

max = 0
L = [0, -1]
R = [0, 1]
U = [-1, 0]
D = [1, 0]
todo = []
curr = [-1, -1]
        
for t in range(4):
    h = len(G)
    for i in range(0, h):
        curr = {0: [h, i], 1:[i,-1], 2:[-1, i], 3:[-1, i]}[t]
        todo.append((curr, t))
        next = False
        v = set()
        nv = set()
        while not next:
            
            if len(todo) == 0:
                for item in v:
                    nv.add(item[:-1])
                if (len(nv)-1) > max:
                    max = len(nv)-1
                next = True
            else:       
                curr, d = todo.pop()
                
            if not str(curr)+str(d) in v:
                v.add(str(curr)+str(d))
                pm = {0:U, 1:R, 2:D, 3:L}[d]
                curr = move(curr, pm)

                if curr[0] < 0 or curr[0] > len(G[0])-1:
                    pass
                elif curr[1] < 0 or curr[1] > len(G)-1:
                    pass
                else:
                    posc = G[curr[0]][curr[1]]
                    
                    if posc == "/":
                        d = {0:1, 1:0, 2:3, 3:2}[d]
                        todo.append((curr, d))
                    elif posc == "\\":
                        d = {0:3, 1:2, 2:1, 3:0}[d]
                        todo.append((curr, d))
                    elif posc == "-":
                        if d == 0 or d == 2:
                            todo.append((curr, 1))
                            todo.append((curr, 3))
                        else:
                            todo.append((curr, d))
                    elif posc == "|":
                        if d == 1 or d == 3:
                            todo.append((curr, 0))
                            todo.append((curr, 2))
                        else:
                            todo.append((curr, d))
                    elif posc == ".":
                        todo.append((curr, d))
        #p1
        if t == 1 and i == 0:
            print(len(nv)-1)
#p2
print(max)
