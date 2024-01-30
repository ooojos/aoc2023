In = open("d19input.txt").read().strip()
rules, wfs = In.split("\n\n")
rules = rules.split("\n")
wfs = wfs.split("\n")
wfl = []
for wf in wfs:
    tmp = wf[1:-1].split(",")
    tmp2 = []
    for x in tmp:
        tmp2.append(int(x[2:]))
    wfl.append(tmp2)

r = {}
for rule in rules:
    name, rest = rule.split("{")
    rest = rest[:-1]
    rest = rest.split(",")
    rl = []
    for cond in rest:
        if ":" in cond:
            c, d = cond.split(":")
            rl.append([c,d])
        else:
            rl.append(["y", cond])
    r[name] = rl




total = 0
for wf in wfl:
    curr = "in"
    while curr != "A" and curr != "R":
        for i, rule in enumerate(r[curr]):
            if rule[0][0] == "y":
                curr = rule[1]
            elif rule[0][0] in "xmas":
                val = wf[{"x":0,"m":1,"a":2,"s":3}[rule[0][0]]]
                if rule[0][1] == "<":
                    if val < int(rule[0][2:]):
                        curr = rule[1]
                        break
                else:
                    if val > int(rule[0][2:]):
                        curr = rule[1]
                        break
    if curr == "A":
        total += sum(wf)
print(total)



items = [1, 4000, 1, 4000, 1, 4000, 1, 4000, "in", ""]
total = 0
Q = []
Q. append(items)
while Q:
    curr = Q.pop()
    currr = curr[8]
    temp = curr.copy()
    temp2 = temp.copy()
    
    if currr == "A":
        num = (temp[1]-temp[0]+1)*(temp[3]-temp[2]+1)*(temp[5]-temp[4]+1)*(temp[7]-temp[6]+1)
        total = total + num
    elif currr == "R":
        pass
    else:
        val = ["n", -1, -1]
        for j, rule in enumerate(r[currr]):
            temp2 = temp.copy()
            #print(f"{j} and {rule}")
            if rule[0][0] == "y":
                temp[9] = temp[9]+" "+temp[8]
                temp[8] = rule[1]
                Q.append(temp)
            if rule[0][0] == "x" and rule[0][1] == "<":
                val = ["x", int(rule[0][2:]), 1]
                if temp[1] > val[1]:
                    temp[1] = val[1] - 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
            if rule[0][0] == "x" and rule[0][1] == ">":
                val = ["x", int(rule[0][2:]), 0]
                if temp[0] < int(rule[0][2:]):
                    temp[0] = int(rule[0][2:]) + 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
                    
            if rule[0][0] == "m" and rule[0][1] == "<":
                val = ["m", int(rule[0][2:]), 1]
                if temp[3] > int(rule[0][2:]):
                    temp[3] = int(rule[0][2:]) - 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
            if rule[0][0] == "m" and rule[0][1] == ">":
                val = ["m", int(rule[0][2:]), 0]
                if temp[2] < int(rule[0][2:]):
                    temp[2] = int(rule[0][2:]) + 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
                    
            if rule[0][0] == "a" and rule[0][1] == "<":
                val = ["a", int(rule[0][2:]), 1]
                if temp[5] > int(rule[0][2:]):
                    temp[5] = int(rule[0][2:]) - 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
            if rule[0][0] == "a" and rule[0][1] == ">":
                val = ["a", int(rule[0][2:]), 0]
                if temp[4] < int(rule[0][2:]):
                    temp[4] = int(rule[0][2:]) + 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)  

            if rule[0][0] == "s" and rule[0][1] == "<":
                val = ["s", int(rule[0][2:]), 1]
                if temp[7] > int(rule[0][2:]):
                    temp[7] = int(rule[0][2:]) - 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
            if rule[0][0] == "s" and rule[0][1] == ">":
                val = ["s", int(rule[0][2:]), 0]
                if temp[6] < int(rule[0][2:], 0):
                    temp[6] = int(rule[0][2:]) + 1
                    temp[9] = temp[9]+" "+temp[8]
                    temp[8] = rule[1]
                    Q.append(temp)
            temp = temp2.copy()
            if val[0] == "x" and val[2] == 1:
                temp[0] = val[1]
            if val[0] == "x" and val[2] == 0:
                temp[1] = val[1]
            if val[0] == "m" and val[2] == 1:
                temp[2] = val[1]
            if val[0] == "m" and val[2] == 0:
                temp[3] = val[1]
            if val[0] == "a" and val[2] == 1:
                temp[4] = val[1]
            if val[0] == "a" and val[2] == 0:
                temp[5] = val[1]
            if val[0] == "s" and val[2] == 1:
                temp[6] = val[1]
            if val[0] == "s" and val[2] == 0:
                temp[7] = val[1]

print(total)
