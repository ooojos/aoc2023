D = open("d6input.txt").readlines()
tlabel, times = D[0].strip().split(":")
dlabel, dists = D[1].strip().split(":")
times = times.strip().split()
dists = dists.strip().split()
times = [int(x) for x in times]
dists = [int(x) for x in dists]
beats = []
b=""
for time in times:
    b = b + str(time)
c=""
for dist in dists:
    c = c + str(dist)

for run, time in enumerate(times):
    total = 0
    for i in range(time):
        journ = i * (time-i)
        if journ > dists[run]:
            total += 1
    beats.append(total)
ans = 1
for t in beats:
    ans = ans * t
print(ans)

total = 0
time = int(b)
dist = int(c)
for i in range(time):
    journ = i * (time-i)
    if journ > dist:
        total = total + 1
print(f"{total} from {b} and {c}")
