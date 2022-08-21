edges=[]
for e in range(500):
  edges.append({})


f = open("edges.txt", "r")
for x in f:
  v1,v2,weight=map(int,x.split())
  v1-=1
  v2-=1
  edges[v1][v2]=weight
  edges[v2][v1]=weight

cost=0
current=0
visited=set()
stack=[[0,0]]
lenn=0
while len(visited)<500:
  hold=stack.pop(0)
  cost+=hold[0]
  current=hold[1]
  visited.add(current)
  for c in edges[current]:
    inStack=False
    if c not in visited:
      for s in range(len(stack)):
        if stack[s][1]==c:
          inStack=True
          if stack[s][0]>edges[current][c]:
            stack[s][0]=edges[current][c]
          break  
      if inStack==False:
        stack.append([edges[current][c],c])
  stack.sort()
print(cost)
