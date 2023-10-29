def minmax(costs, fruits):
    costs.sort()
    frts = {}
    mincost = 0
    max_cost = 0
    
    for fruit in fruits:
        try:
            frts[fruit] += 1
        except:
            frts[fruit] = 1
    sfrts = dict(sorted(frts.items(), key=lambda x: x[1], reverse=True))
    i = 0
    j = len(costs)-1
    for fr in sfrts:
        mincost += costs[i]*sfrts[fr]
        max_cost += costs[j]*sfrts[fr]
        i += 1
        j -=1
    print(str(mincost)+ ' '+str(max_cost))
    
a, b = map(int, input().split())
fruits = []
costs = [int(i) for i in input().split()]
for _ in range(b):
    fruits.append(input().strip())
minmax(costs, fruits)

        
    
    
    
    