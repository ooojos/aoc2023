import re

In = open("d15input.txt").read().strip()
In = In.split(",")

total = 0


for word in In:
    cv = 0
    for ch in word:
        cv = cv + ord(ch)
        cv = cv * 17
        cv = cv % 256
    total += cv
print(total)


boxes = [dict() for x in range(256)]
for word in In:
    kw, kn = re.split("=|-", word)
    cv = 0
    for ch in word:
        if ch == "=":
            boxes[cv][kw] = kn
        elif ch == "-":
            if kw in boxes[cv]:
                boxes[cv].pop(kw)
        else:
            cv = cv + ord(ch)
            cv = cv * 17
            cv = cv % 256

total = 0
for bn, box in enumerate(boxes):
    for slot, item in enumerate(box):
        fp = (bn+1) * (slot+1) * int(box[item])
        total = total + fp
print(total)
