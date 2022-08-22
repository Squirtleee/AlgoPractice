# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1714/submission/166687858
'''
Question Link: https://codeforces.com/contest/1714/problem/G 
(!! Super recommend looking clicking on the link cuz the graphs made the problem much easier to understand !!)

You are given a rooted tree. It contains 𝑛 vertices, which are numbered from 1 to 𝑛. The root is the vertex 1.

Each edge has two positive integer values. Thus, two positive integers 𝑎𝑗 and 𝑏𝑗 are given for each edge.

Output 𝑛−1 numbers 𝑟2,𝑟3,…,𝑟𝑛, where 𝑟𝑖 is defined as follows.

Consider the path from the root (vertex 1) to 𝑖 (2≤𝑖≤𝑛). Let the sum of the costs of 𝑎𝑗 along this path be 𝐴𝑖. Then 𝑟𝑖 is equal to the length of the maximum prefix of this path such that the sum of 𝑏𝑗 along this prefix does not exceed 𝐴𝑖.

Input
The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases in the test.

The descriptions of test cases follow.

Each description begins with a line that contains an integer 𝑛 (2≤𝑛≤2⋅105) — the number of vertices in the tree.

This is followed by 𝑛−1 string, each of which contains three numbers 𝑝𝑗,𝑎𝑗,𝑏𝑗 (1≤𝑝𝑗≤𝑛; 1≤𝑎𝑗,𝑏𝑗≤109) — the ancestor of the vertex 𝑗, the first and second values an edge that leads from 𝑝𝑗 to 𝑗. The value of 𝑗 runs through all values from 2 to 𝑛 inclusive. It is guaranteed that each set of input data has a correct hanged tree with a root at the vertex 1.

It is guaranteed that the sum of 𝑛 over all input test cases does not exceed 2⋅105.

Output
For each test case, output 𝑛−1 integer in one line: 𝑟2,𝑟3,…,𝑟𝑛.
'''
'''
Sample Input:
1
9
1 5 6
4 5 1
2 9 10
4 2 1
1 2 1
2 3 3
6 4 3
8 1 3
Sample Output:
0 3 1 2 1 1 2 3 
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  nodes=int(input())
  graph={}
  big1=[0]*(nodes+1)
  ans=[0]*(nodes+1)
  for y in range(1,nodes+1):
    graph[y]=[]
    
  for u in range(2,nodes+1):
    parent,edge1,edge2=map(int,input().split())
    graph[parent].append([u,edge1,edge2])

  stack=deque()
  for n in graph[1]:
    n2=n+[0,0]
    stack.append(n2)
  while stack:
    current=stack.popleft()
    big1[current[0]]=current[3]+current[1]
    for s in graph[current[0]]:
      x=s
      x=x+[current[3]+current[1],current[4]+1]
      stack.append(x)

  stack=deque()
  for n in graph[1]:
    stack.append(n)
  path=deque()
  visited=set()
  before=set()
  while stack:
    current=stack.pop()
    if current[0] not in before:
      if len(path)>0:
        path.append(current[2]+path[-1])
      else:
        path=[current[2]]
    before.add(current[0])
    total=0
    ind=0
    new=False
    for s in graph[current[0]]:
      if s[0] not in visited:
        new=True
    if new==False:
      visited.add(current[0])
      left=0
      right=len(path)
      while left<right:
        mid=(left+right)//2
        if path[mid]<big1[current[0]]:
          left=mid+1
        else:
          right=mid
      if left==len(path):
        left-=1
      total=path[left]
      if total>big1[current[0]]:
        ans[current[0]]=(left)
      else:
        ans[current[0]]=(left+1)
      path.pop()
    else:
      stack.append(current)
      for s in graph[current[0]]:
        if s[0] not in visited:
          stack.append(s)

  for r in range(2,nodes+1):
    print(ans[r],end=' ')
  print('')
