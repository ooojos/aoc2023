with open("d5input.txt") as lines:
    p1seeds = []
    seeds = []
    mappings = []
    section = []
    locs = []
    
    for i, line in enumerate(lines):
        if i == 0:
            label, seednums = line.split(":")
            seeds = seednums.split()
            seeds = [int(x) for x in seeds]
            p1seeds = [int(x) for x in seeds]
            for i, seed in enumerate(seeds):
                if i % 2 == 1:
                    seeds[i] = seeds[i]+seeds[i-1]
        else:
            if len(line) > 0:
                if line[0].isdigit():
                    indiv = line.split()
                    indiv = [int(x) for x in indiv]
                    section.append(indiv)
            if len(line.strip()) == 0:
                mappings.append(section)
                section=[]
                    
    for seed in p1seeds:
        tseed = seed
        for section in mappings:
            done = False
            for trans in section:
                if tseed >= trans[1] and tseed <= trans[1]+trans[2] and not done:
                    tseed = tseed + trans[0]-trans[1]
                    done = True
        locs.append(tseed)
    print(min(locs))
    for i, section in enumerate(mappings):
        for trans in section:
            cand = trans[1]
            tseed = trans[0]
            j=i+1
            while j < len(mappings):
                done = False
                for options in mappings[j]:
                    if tseed >= options[1] and tseed <= options[1]+options[2] and not done:
                        tseed = tseed + options[0]-options[1]
                        done = True
                j=j+1
            j=i-1
            
            seedcand = cand
            while j>=0:
                done = False
                for options in mappings[j]:
                    if seedcand >= options[0] and seedcand <= options[0]+options[2] and not done:
                        seedcand = seedcand + options[1]-options[0]
                        done = True
                j=j-1
            for m in range(0, len(seeds), 2):
                if seedcand >= seeds[m] and seedcand <= seeds[m+1]:
                    locs.append(tseed)
    print(min(locs))
