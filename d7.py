hands = open("d7input.txt").readlines()
shands = [[],[],[],[],[],[],[]]

for i, play in enumerate(hands):
    hand, bid = play.split()
    vals = [0] * 13
    nhand = hand
    nhand = nhand.replace("K", "B")
    nhand = nhand.replace("Q", "C")
    nhand = nhand.replace("J", "M")
    nhand = nhand.replace("T", "D")
    nhand = nhand.replace("9", "E")
    nhand = nhand.replace("8", "F")
    nhand = nhand.replace("7", "G")
    nhand = nhand.replace("6", "H")
    nhand = nhand.replace("5", "I")
    nhand = nhand.replace("4", "J")
    nhand = nhand.replace("3", "K")
    nhand = nhand.replace("2", "L")

    vals = [0]*13

    for c in nhand:
        n = ord(c)-65
        vals[n]+=1
    mv = 0
    mvi = -1
    for s in range(len(vals)-1):
        if vals[s]> mv:
            mv = vals[s]
            mvi = s
    if mvi == -1:
        vals[0] = 5
    else:
        vals[mvi] = vals[mvi] + vals[12]
        vals[12] = 0  
    
    if max(vals) == 5:
        shands[0].append(nhand + " " + bid)
        
    elif max(vals) == 4:
        shands[1].append(nhand + " " + bid)
    elif max(vals) == 3:
        for j in range(len(vals)):
            if vals[j]== 2:
                shands[2].append(nhand + " " + bid)
                break
            elif vals[j] == 1:
                shands[3].append(nhand + " " + bid)
                break
    elif max(vals) == 2:
        tpair = False
        numos = 0
        for j in range(len(vals)):
            if vals[j] == 0:
                numos+=1
        if numos == 10:
            shands[4].append(nhand + " " + bid)
        elif numos == 9:
            shands[5].append(nhand + " " + bid)
    else:
        shands[6].append(nhand + " " + bid)
      
for shand in shands:
    shand.sort()


total = 0
i = len(hands)

for shand in shands:
    for hand in shand:
        bid = int(hand.split()[1])
        val = i*bid
        total = total + val
        print(f"{i}    {bid}    {hand}    {val}     {total}")
        i = i - 1


print(total)
