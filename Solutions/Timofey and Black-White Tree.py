# Time Limit per Test: 4 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1790/submission/191028063
'''
Quesiton Link: https://codeforces.com/contest/1790/problem/F

Timofey came to a famous summer school and found a tree on 𝑛
 vertices. A tree is a connected undirected graph without cycles.

Every vertex of this tree, except 𝑐0
, is colored white. The vertex 𝑐0
 is colored black.

Timofey wants to color all the vertices of this tree in black. To do this, he performs 𝑛−1
 operations. During the 𝑖
-th operation, he selects the vertex 𝑐𝑖
, which is currently white, and paints it black.

Let's call the positivity of tree the minimum distance between all pairs of different black vertices in it. The distance between the vertices 𝑣
 and 𝑢
 is the number of edges on the path from 𝑣
 to 𝑢
.

After each operation, Timofey wants to know the positivity of the current tree.

Input
The first line contains the integer 𝑡
 (1≤𝑡≤104
) — the number of testcases.

The first line of each testcase contains the integers 𝑛,𝑐0
 (2≤𝑛≤2⋅105
, 1≤𝑐0≤𝑛
) — the number of vertices in the tree and index of the initial black vertex.

The second line of each testcase contains 𝑛−1
 unique integers 𝑐1,𝑐2,…,𝑐𝑛−1
 (1≤𝑐𝑖≤𝑛
, 𝑐𝑖≠𝑐0
), where 𝑐𝑖
 is the vertex which is colored black during the 𝑖
-th operation.

Each of the next 𝑛−1
 row of each testcase contains the integers 𝑣𝑖,𝑢𝑖
 (1≤𝑣𝑖,𝑢𝑖≤𝑛
) — edges in the tree.

It is guaranteed that the sum of 𝑛
 for all testcases does not exceed 2⋅105
.

Output
For each testcase, print 𝑛−1
 integer on a separate line.

The integer with index 𝑖
 must be equal to positivity of the tree obtained by the first 𝑖
 operations.
'''
'''
Sample Input:
6
6 6
4 1 3 5 2
2 4
6 5
5 3
3 4
1 3
4 2
4 1 3
3 1
2 3
1 4
10 3
10 7 6 5 2 9 8 1 4
1 2
1 3
4 5
4 3
6 4
8 7
9 8
10 8
1 8
7 3
7 5 1 2 4 6
1 2
3 2
4 5
3 4
6 5
7 6
9 7
9 3 1 4 2 6 8 5
4 1
8 9
4 8
2 6
7 3
2 4
3 5
5 4
10 2
1 8 5 10 6 9 4 3 7
10 7
7 8
3 6
9 7
7 6
4 2
1 6
7 5
9 2
Sample Output:
3 2 1 1 1 
3 1 1 
3 2 2 2 2 2 1 1 1 
4 2 2 1 1 1 
5 1 1 1 1 1 1 1 
4 3 2 2 1 1 1 1 1 
'''
import sys
input = sys.stdin.readline

from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc

@bootstrap
def dfs(cur,parent,dist):
  par[cur]=parent
  for k in edge[cur]:
    if k !=parent:
      if dist+1<dis[k]:
        dis[k]=dist+1
        #print(dis)
        yield dfs(k,cur,dist+1)
  yield None
  

rounds = int(input())
for ii in range(rounds):
  out=0
  ver,start=map(int,input().split())
  seq=list(map(int,input().split()))
  edge={}
  start-=1
  par=[-1]*(ver)
  for v in range(ver-1):
    seq[v]-=1
  dis=[10**20]*(ver)
  dis[start]=0
  for v in range(ver-1):
    v1,v2=map(int,input().split())
    v1-=1
    v2-=1
    if v1 not in edge:
      edge[v1]=set()
    if v2 not in edge:
      edge[v2]=set()
    edge[v1].add(v2)
    edge[v2].add(v1)
  dfs(start,-1,0)
  ans=[1]*(ver-1)
  for v in range(ver-1):
    ans[v]=dis[seq[v]]
    #print(ans,dis[seq[v]],seq[v],dis)
    if v>0 and ans[v]>ans[v-1]:
      ans[v]=ans[v-1]
    pa=par[seq[v]]
    cnt=1
    dis[seq[v]]=0
    while pa!=-1:
      if ans[v]>dis[pa]+cnt:
        ans[v]=dis[pa]+cnt
      if cnt>=dis[pa] or (v>0 and cnt>ans[v-1]):
        break
      dis[pa]=min(cnt,dis[pa])
      cnt+=1
      pa=par[pa]
    if ans[v]==1:
      break
  for a in ans:
    print(a,end=' ')
  print('')
