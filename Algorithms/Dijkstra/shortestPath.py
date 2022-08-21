# Dijkstra's shortest-path algorithm
# It is known that there exists a path betwenn node 0 to every other node

mapp=[]
vertex=200

# Graph Setup
for v in range(vertex):
  mapp.append([])
for i in range(vertex):
  row=input().split()
  if len(row)>0:
    current=int(row[0])
    has_path=set()
    #nodes are labeled 1~200 but I want to do 0~199
    current-=1
    for m in range(1,len(row)):
      connected,distance=row[m].split(',')
      connected=int(connected)
      has_path.add(connected)
      #nodes are labeled 1~200 but I want to do 0~199
      connected-=1
      distance=int(distance)
      mapp[current].append([connected,distance])
    '''for n in range(vertex):
      if n not in has_path:
        mapp[current].append([n,10**10])'''
# Compute Shortest Path
start_node=0
shortest_dist={}
visited=set()
queue=[[0,start_node]]

while len(visited)<vertex:
  queue.sort()
  current=queue.pop(0)
  distance=current[0]
  current_node=current[1]
  visited.add(current_node)
  shortest_dist[current_node]=distance
  for connected in mapp[current_node]:
    next_node=connected[0]
    edge=connected[1]
    if next_node not in visited:
      in_queue=False
      #check if in queue, if in queue see if better, else append in queue
      for q in range(len(queue)):
        if queue[q][1]==next_node:
          in_queue=True
          if queue[q][0]>edge+distance:
            queue[q][0]=edge+distance
      if in_queue==False:
        queue.append([edge+distance,next_node])
want=int(input('Which vertex are you asking abt??'))
print(shortest_dist[want])
