with open("d2input.txt") as text:
    lines = text.read().strip().split("\n")
    total = 0
    total2 = 0
    rgb = [0,0,0]
    for game, line in enumerate(lines, start=1):
        a = line[line.find(" ")+1:]
        a = a[a.find(" ")+1:]
        draws = a.split(";")
        for draw in draws:
            indiv = draw.split(",")
            for pair in indiv:
                pair = pair.strip()
                val, colour = pair.split(" ")
                val = int(val)
                if colour == "red" and val > rgb[0]:
                    rgb[0] = val
                if colour == "green" and val > rgb[1]:
                    rgb[1] = val
                if colour == "blue" and val > rgb[2]:
                    rgb[2] = val
        if rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14:
            total = total + game
        power = rgb[0] * rgb[1] * rgb[2]
        total2 = total2 + power
        rgb = [0,0,0]
    print(total)
    print (total2)
        
