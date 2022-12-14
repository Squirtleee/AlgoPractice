# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1689/submission/160213221
'''
Question Link: https://codeforces.com/contest/1689/problem/C

Byteland is a beautiful land known because of its beautiful trees.

Misha has found a binary tree with ๐ vertices, numbered from 1 to ๐. A binary tree is an acyclic connected bidirectional graph containing ๐ vertices and ๐โ1 edges. Each vertex has a degree at most 3, whereas the root is the vertex with the number 1 and it has a degree at most 2.

Unfortunately, the root got infected.

The following process happens ๐ times:

Misha either chooses a non-infected (and not deleted) vertex and deletes it with all edges which have an end in this vertex or just does nothing.
Then, the infection spreads to each vertex that is connected by an edge to an already infected vertex (all already infected vertices remain infected).
As Misha does not have much time to think, please tell him what is the maximum number of vertices he can save from the infection (note that deleted vertices are not counted as saved).

Input
There are several test cases in the input data. The first line contains a single integer ๐ก (1โค๐กโค5000) โ the number of test cases. This is followed by the test cases description.

The first line of each test case contains one integer ๐ (2โค๐โค3โ105) โ the number of vertices of the tree.

The ๐-th of the following ๐โ1 lines in the test case contains two positive integers ๐ข๐ and ๐ฃ๐ (1โค๐ข๐,๐ฃ๐โค๐), meaning that there exists an edge between them in the graph.

It is guaranteed that the graph is a binary tree rooted at 1. It is also guaranteed that the sum of ๐ over all test cases won't exceed 3โ105.

Output
For each test case, output the maximum number of vertices Misha can save.
'''
'''
Sample Input:
2
2
1 2
4
1 2
2 3
2 4
Sample Output:
0
2
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  vertex=int(input())
  dir={}
  for j in range(vertex-1):
    a,b=map(int,input().split())
    if a in dir:
      dir[a].append(b)
    else:
      dir[a]=[b]
    if b in dir:
      dir[b].append(a)
    else:
      dir[b]=[a]
  queue=[[1,0]]
  level=0
  saved=0
  visited=set()
  min_l=10**100
  while len(queue)>0:
    hold=queue.pop(0)
    node=hold[0]
    visited.add(node)
    l=hold[1]
    if l<min_l:
      min_l=l
    child=0
    for x in dir[node]:
      if x not in visited:
        queue.append([x,l+1])
        child+=1
    if child<=1:
      saved=max(saved,vertex-(2*(l)+1+child))
      if child==0:
        break
  print(saved)
