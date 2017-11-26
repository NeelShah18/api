import sys
import math
import random
from gurobipy import *

#deciding final optimal path among differetn choices
def final_path(ver):
    t = [False]*n
    lc = []
    el = []
    final = [[] for i in range(n)]
    for x,y in ver:
        final[x].append(y)
    while True:
        cur = t.index(False)
        cycle = [cur]
        while True:
            t[cur] = True
            neighbors = [x for x in final[cur] if not t[x]]
            if len(neighbors) == 0:
                break
            cur = neighbors[0]
            cycle.append(cur)
        lc.append(cycle)
        el.append(len(cycle))
        if sum(el) == n:
            break
    return lc[el.index(min(el))]

#finding optimal path
def opt_sub(m, diss):
    if diss == GRB.Callback.MIPSOL:
        sel = []
        
        for i in range(n):
            sol = m.cbGetSolution([m._vars[i,j] for j in range(n)])
            sel += [(i,j) for j in range(n) if sol[j] > 0.5]
        
        tour = final_path(sel)
        if len(tour) < n:
            expr = 0
            for i in range(len(tour)):
                for j in range(i+1, len(tour)):
                    expr += m._vars[tour[i], tour[j]]
            m.cbLazy(expr <= len(tour)-1)

# Calculating optimal distance
def final_dis(po, i, j):
    x = po[i][0] - po[j][0]
    y = po[i][1] - po[j][1]
    return math.sqrt(x*x + y*y)

if len(sys.argv) < 2:
    lol = 1
    exit(1)
n = int(sys.argv[1])

random.seed(1)
points = []
for i in range(n):
    points.append((random.randint(0,100),random.randint(0,100)))

#Starting of gurobi module
m = Model()

vars = {}
for i in range(n):
    for j in range(i+1):
        vars[i,j] = m.addVar(obj=final_dis(points, i, j), vtype=GRB.BINARY,
                             name='e'+str(i)+'_'+str(j))
        vars[j,i] = vars[i,j]
m.update()


for i in range(n):
    m.addConstr(quicksum(vars[i,j] for j in range(n)) == 2)
    vars[i,i].ub = 0
m.update()


m._vars = vars
m.params.LazyConstraints = 1
m.optimize(opt_sub)

final_sol = m.getAttr('x', vars)
ans = [(i,j) for i in range(n) for j in range(n) if final_sol[i,j] > 0.5]

assert len(final_path(ans)) == n

print('')
print('Optimal tour: %s' % str(final_path(ans)))