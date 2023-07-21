def ISS(n):
    d = [float('inf')] * n 
    d[0] = 0
    return d

def relax(d, u, v, energia):
    if d[v] > d[u] + energia[v]:
        if 100 + d[u] + energia[v] > 0:
            d[v] = d[u] + energia[v]
        
def bellman(arestas, energia, n):
    d = ISS(n)
    i = 0
    while i < n - 1:
        for j in range(len(arestas)):
            relax(d, arestas[j][0], arestas[j][1], energia)
        i += 1
    return d
    
n = int(input())
energia = [int(i) for i in input().split(" ")]
m = int(input())
arestas = []
for i in range(m):
    u, v = map(int, input().split(" "))
    arestas.append((u, v, energia[v]))
    
d = bellman(arestas, energia, n)

if d[len(d) - 1] == float('inf'):
    print('impossible')
else:
    print('possible')