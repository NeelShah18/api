import sys
import math
import random
from gurobipy import *

def subtourelim(model, where):
    if where == GRB.Callback.MIPSOL:
        selected = []
        
        for i in range(n):
            sol = model.cbGetSolution([model._vars[i,j] for j in range(n)])
            selected += [(i,j) for j in range(n) if sol[j] > 0.5]
        
        tour = subtour(selected)
        if len(tour) < n:
            expr = 0
            for i in range(len(tour)):
                for j in range(i+1, len(tour)):
                    expr += model._vars[tour[i], tour[j]]
            model.cbLazy(expr <= len(tour)-1)


def distance(points, i, j):
    dx = points[i][0] - points[j][0]
    dy = points[i][1] - points[j][1]
    return math.sqrt(dx*dx + dy*dy)


def subtour(edges):
    visited = [False]*n
    cycles = []
    lengths = []
    selected = [[] for i in range(n)]
    for x,y in edges:
        selected[x].append(y)
    while True:
        current = visited.index(False)
        thiscycle = [current]
        while True:
            visited[current] = True
            neighbors = [x for x in selected[current] if not visited[x]]
            if len(neighbors) == 0:
                break
            current = neighbors[0]
            thiscycle.append(current)
        cycles.append(thiscycle)
        lengths.append(len(thiscycle))
        if sum(lengths) == n:
            break
    return cycles[lengths.index(min(lengths))]

if len(sys.argv) < 2:
    lol = 1
    exit(1)
n = int(sys.argv[1])

random.seed(1)
points = []
for i in range(n):
    points.append((random.randint(0,100),random.randint(0,100)))

m = Model()


vars = {}
for i in range(n):
    for j in range(i+1):
        vars[i,j] = m.addVar(obj=distance(points, i, j), vtype=GRB.BINARY,
                             name='e'+str(i)+'_'+str(j))
        vars[j,i] = vars[i,j]
m.update()


for i in range(n):
    m.addConstr(quicksum(vars[i,j] for j in range(n)) == 2)
    vars[i,i].ub = 0
m.update()


m._vars = vars
m.params.LazyConstraints = 1
m.optimize(subtourelim)

solution = m.getAttr('x', vars)
selected = [(i,j) for i in range(n) for j in range(n) if solution[i,j] > 0.5]
assert len(subtour(selected)) == n

print('')
print('Optimal tour: %s' % str(subtour(selected)))
print('')