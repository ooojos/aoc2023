with open("d4input.txt") as text:
    total = 0
    numcards = []
    for cardnum, line in enumerate(text):
        if cardnum >= len(numcards):
            numcards.append(1)
        winset = set()
        winlist = line[line.find(":")+1: line.find("|")-1].strip().split()
        winset = set(winlist)
        havelist = line[line.find("|")+1:].strip().split()
        score = 0
        for guess in havelist:
            if guess in winset:
                score = score + 1
        for j in range(score):
            if cardnum+j+1 >=len(numcards):
                numcards.append(1)
            numcards[cardnum+j+1] += numcards[cardnum]
        if score != 0:
            total = total + 2**(score-1)
    print(total)
    print(sum(numcards))
        
