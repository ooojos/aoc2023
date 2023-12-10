In = open("d9input.txt").read().strip()
In = In.split("\n")

red = []
lt = []
lt2 = []
firsts = []
for line in In:
    nums = line.split()
    nums = [int(x) for x in nums]
    total = 0
    firsts = []
    while not (all(y==0 for y in nums)):
        firsts.append(nums[0])
        total = total + nums[-1]
        for i in range(len(nums) - 1):
            red.append(nums[i+1] - nums[i])
        nums = red
        red = []
    lt.append(total)
    t2 = 0
    for j in range(len(firsts)-1, -1, -1):
        t2 = firsts[j] - t2
    lt2.append(t2)

print(sum(lt))
print(sum(lt2))        
