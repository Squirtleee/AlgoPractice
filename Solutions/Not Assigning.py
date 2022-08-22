# Time Limit per Test: 1.5 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1627/submission/162699853
'''
Question Link: https://codeforces.com/contest/1627/problem/C

You are given a tree of 𝑛 vertices numbered from 1 to 𝑛, with edges numbered from 1 to 𝑛−1. A tree is a connected undirected graph without cycles. You have to assign integer weights to each edge of the tree, such that the resultant graph is a prime tree.

A prime tree is a tree where the weight of every path consisting of one or two edges is prime. A path should not visit any vertex twice. The weight of a path is the sum of edge weights on that path.

Consider the graph below. It is a prime tree as the weight of every path of two or less edges is prime. For example, the following path of two edges: 2→1→3 has a weight of 11+2=13, which is prime. Similarly, the path of one edge: 4→3 has a weight of 5, which is also prime.


Print any valid assignment of weights such that the resultant tree is a prime tree. If there is no such assignment, then print −1. It can be proven that if a valid assignment exists, one exists with weights between 1 and 105 as well.

Input
The input consists of multiple test cases. The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases. The description of the test cases follows.

The first line of each test case contains one integer 𝑛 (2≤𝑛≤105) — the number of vertices in the tree.

Then, 𝑛−1 lines follow. The 𝑖-th line contains two integers 𝑢 and 𝑣 (1≤𝑢,𝑣≤𝑛) denoting that edge number 𝑖 is between vertices 𝑢 and 𝑣. It is guaranteed that the edges form a tree.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
For each test case, if a valid assignment exists, then print a single line containing 𝑛−1 integers 𝑎1,𝑎2,…,𝑎𝑛−1 (1≤𝑎𝑖≤105), where 𝑎𝑖 denotes the weight assigned to the edge numbered 𝑖. Otherwise, print −1.

If there are multiple solutions, you may print any.
'''
'''
Sample Input:
3
2
1 2
4
1 3
4 3
2 1
7
1 2
1 3
3 4
3 5
6 2
7 2
Sample Output:
17
2 5 11
-1
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  vertex=int(input())
  edge2=[]
  order={}
  for v in range(vertex):
    edge2.append([])
  for x in range(vertex-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    order[(a,b)]=x
    edge2[a].append(b)
    edge2[b].append(a)
  nope=False
  for ed in edge2:
    if len(ed)>2:
      nope=True
      break
  if nope:
    print(-1)
  elif vertex==2:
    print(7)
  elif vertex==3:
    print(2,17)
  else:
    start=-1
    end=-1
    for e in range(len(edge2)):
      if len(edge2[e])==1:
        if start==-1:
          start=e
        else:
          end=e
    out_order=[0]*(vertex-1)
    visited=set()
    visited.add(start)
    cnt=0
    while end not in visited:
      ori=start
      for ver in edge2[start]:
        if ver not in visited:
          start=ver
      visited.add(start)
      if cnt%2==0:
        cnt+=1
        if (start,ori) in order:
          out_order[order[(start,ori)]]=2
        else:
          out_order[order[(ori,start)]]=2
      else:
        cnt+=1
        if (start,ori) in order:
          out_order[order[(start,ori)]]=3
        else:
          out_order[order[(ori,start)]]=3
    for o in out_order:
      print(o,end=' ')
    print('')
