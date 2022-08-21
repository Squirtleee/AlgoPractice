'''
Question: Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kk of clusters is set to 4.  What is the maximum spacing of a 4-clustering?
'''
'''
So basically my idea was to modify the Kruskal's MST algorithm and apply it to clustering.
'''
edge=[]
for i in range(500):
  temp=[0]*500
  edge.append(temp)


data=[]
f=open("/Users/jesshuang/Desktop/CS/Courses/data1.txt","r")
for x in f:
  n1,n2,cost=map(int,x.split())
  n1-=1
  n2-=1
  data.append([cost,n1,n2])
  edge[n1][n2]=cost
  edge[n2][n1]=cost

rec=[]

groups=[]
for y in range(500):
  groups.append({y})

visited=0
data.sort()
ind=0
while len(groups)>4:
  da=data[ind]
  ind+=1
  in1=-5
  in2=-5
  leng=len(groups)
  for g in range(leng):
    if da[1] in groups[g]:
      in1=g
    if da[2] in groups[g]:
      in2=g
  if in1!=in2:   
    for ve in groups[in2]:
      groups[in1].add(ve)
    groups.pop(in2)

spacing=10**100
for e in (edge[383]):
  if e<spacing and e>0:
    spacing=e
for e in (edge[413]):
  if e<spacing and e>0:
    spacing=e
for e in (edge[461]):
  if e<spacing and e>0:
    spacing=e
print(spacing,groups)
