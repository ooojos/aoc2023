In = open("d13input.txt").read()
In = In.split("\n\n")


def p(g):
    for line in g:
        print(line)

total = 0
t2=0
for grid in In:
#    print("next grid")
    a = grid.split()
    i = 0
    while i < len(a[0])-1:
        works = True
        errors = 0
        for ln, line in enumerate(a):
            j = i
            k = i+1
            while j >= 0 and k <= len(line)-1:
                if line[j] != line[k]:
                    works = False
                    errors+=1
                j -= 1
                k += 1
        if works:
#            print(f"vert at {i+1}")
            total = total + i + 1
        if errors == 1:
            t2 = t2 + i + 1
        i+=1

#print("looking for horiz")
for grid in In:
    a = grid.split()
    i = 0
    while i < len(a)-1:
        works = True
        errors = 0
        n = 0
        while n < len(a[0]):
            j = i
            k = i+1
            while j >= 0 and k < len(a):
                if a[j][n] != a[k][n]:
                    works = False
                    errors += 1
                j -= 1
                k += 1

            n += 1
        if works:
            total += (i+1)*100
#            print(f"horiz at {i+1}")
        if errors == 1:
            t2 += (i+1)*100
        i += 1
    
print(total)
print(t2)
