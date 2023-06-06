# Time Limit per Test: 1 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1818/submission/204177506
'''
Question Link: https://codeforces.com/contest/1818/problem/D

You are given a simple undirected graph with 𝑛
 nodes and 𝑚
 edges. Note that the graph is not necessarily connected. The nodes are labeled from 1
 to 𝑛
.

We define a graph to be a Fish Graph if it contains a simple cycle with a special node 𝑢
 belonging to the cycle. Apart from the edges in the cycle, the graph should have exactly 2
 extra edges. Both edges should connect to node 𝑢
, but they should not be connected to any other node of the cycle.

Determine if the graph contains a subgraph that is a Fish Graph, and if so, find any such subgraph.

In this problem, we define a subgraph as a graph obtained by taking any subset of the edges of the original graph.

Visualization of example 1. The red edges form one possible subgraph that is a Fish Graph.
Input
The first line of input contains the integer 𝑡
 (1≤𝑡≤1000
), the number of test cases. The description of test cases follows.

The first line of each test case contains two integers, 𝑛
 and 𝑚
 (1≤𝑛,𝑚≤2000
) — the number of nodes and the number of edges.

Each of the next 𝑚
 lines contains the description of an edge. Each line contains two integers 𝑢𝑖
 and 𝑣𝑖
 (1≤𝑢𝑖,𝑣𝑖≤𝑛
, 𝑢𝑖≠𝑣𝑖
) — an edge connects node 𝑢𝑖
 to node 𝑣𝑖
.

It is guaranteed that no two edges connect the same unordered pair of nodes.

Furthermore, it is guaranteed that the sum of 𝑛
 and the sum of 𝑚
 over all test cases both do not exceed 2000
.

Output
For each testcase, output "YES" if the graph contains a subgraph that is a Fish Graph, otherwise print "NO". If the answer is "YES", on the following lines output a description of the subgraph.

The first line of the description contains one integer 𝑘
 — the number of edges of the subgraph.

On the next 𝑘
 lines, output the edges of the chosen subgraph. Each of the 𝑘
 lines should contains two integers 𝑢
 and 𝑣
 (1≤𝑢,𝑣≤𝑛
, 𝑢≠𝑣
) — the edge between 𝑢
 and 𝑣
 belongs to the subgraph. The order in which 𝑢
 and 𝑣
 are printed does not matter, as long as the two nodes are connected by an edge in the original graph. The order in which you print the edges does not matter, as long as the resulting subgraph is a fish graph.

If there are multiple solutions, print any.
'''
'''
Sample Input:
3
7 8
1 2
2 3
3 4
4 1
4 5
4 6
4 2
6 7
7 7
6 7
1 2
2 3
3 4
4 1
1 3
3 5
4 4
1 3
3 4
4 1
1 2
Sample Output:
YES
6
5 4
6 4
4 3
1 4
2 1
3 2
YES
5
5 3
2 3
3 1
4 3
1 4
NO
'''
import sys
from collections import deque
def input():
  return sys.stdin.readline()[:-1]
t=int(input())




for _ in range(t):
  n,m=map(int,input().split())
  G=[[] for _ in range(n)]
  for i in range(m):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  
  def bfs(G,s):
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if y not in visited:
          visited.add(y)
          dq.append(y)
          if y!=s and y in tmp:
            return y
  
  from collections import deque
  def bfs2(G,s,i):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if y==i: continue
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  ans='No'
  for i in range(n):
    if ans=='Yes': break
    if len(G[i])<4: continue
    tmp=set(G[i])
    visited=set()
    visited.add(i)
    for j in G[i]:
      y=bfs(G,j)
      if y!=None:
        ans='Yes'
        D=bfs2(G,j,i)
        # print(D,i,j,y)
        now=y
        ans2=[(i,j),(i,y)] #two edges in the cycle
        for k in G[i]:
          if k!=j and k!=y: ans2.append((i,k)) # two extra edges
          if len(ans2)==4: break
        for k in range(D[y]):
          for l in G[now]:
            if D[l]==D[now]-1:
              ans2.append((l,now))
              now=l
              break
        break
  print(ans)
  if ans=='Yes':
    print(len(ans2))
    for i in range(len(ans2)):
      print(ans2[i][0]+1,ans2[i][1]+1)
