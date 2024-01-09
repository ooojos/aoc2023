import networkx as nx
import random
import matplotlib.pyplot as plt

In = open("d25test.txt").read().strip()
In = In.split("\n")

g = nx.Graph()
for line in In:
    at, tos = line.split(":")
    for to in tos.strip().split(' '):
        g.add_edge(at, to, capacity=1)



nx.draw_networkx(g)
plt.show()

while True:

    start = random.choice(list(g.nodes))
    end = random.choice(list(g.nodes))
    cut, part = nx.minimum_cut(g, start, end)
    if cut == 3:
        print(len(part[0])*len(part[1]))
        break
