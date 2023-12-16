#Doesn't acurrately check corners
#(also is slow and badly written)

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
    for i in range(0, len(G)):

        if t == 0:
            curr = [i, len(G)]
            d = 3
        elif t == 1:
            curr = [i, -1]
            d = 1
        elif t == 2:
            curr = [-1, i]
            d = 2
        elif t == 3:
            curr = [len(G), i]
            d = 0
        
        todo.append((curr, d))
        

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
                if d == 0:
                    curr = move(curr, U)
                elif d == 1:
                    curr = move(curr, R)
                elif d == 2:
                    curr = move(curr, D)
                elif d == 3:
                    curr = move(curr, L)

                if curr[0] < 0 or curr[0] > len(G[0])-1:
                    pass
                elif curr[1] < 0 or curr[1] > len(G)-1:
                    pass
                else:
                    posc = G[curr[0]][curr[1]]
                    
                    if posc == "/":
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                        todo.append((curr, d))
                    elif posc == "\\":
                        if d == 0:
                            d = 3
                        elif d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 0
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

print(max)
