# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1825/submission/206296067
'''
Question Link: https://codeforces.com/contest/1825/problem/D1

LuoTianyi now lives in a world with 𝑛
 floating islands. The floating islands are connected by 𝑛−1
 undirected air routes, and any two of them can reach each other by passing the routes. That means, the 𝑛
 floating islands form a tree.

One day, LuoTianyi wants to meet her friends: Chtholly, Nephren, William, .... Totally, she wants to meet 𝑘
 people. She doesn't know the exact positions of them, but she knows that they are in pairwise distinct islands. She define an island is good if and only if the sum of the distances†
 from it to the islands with 𝑘
 people is the minimal among all the 𝑛
 islands.

Now, LuoTianyi wants to know that, if the 𝑘
 people are randomly set in 𝑘
 distinct of the 𝑛
 islands, then what is the expect number of the good islands? You just need to tell her the expect number modulo 109+7
.

†
The distance between two islands is the minimum number of air routes you need to take to get from one island to the other.

Input
The first line contains two integers 𝑛
 and 𝑘
 (1≤𝑘≤min(𝑛,3),1≤𝑛≤2⋅105
) — the number of the islands and people respectively.

Next 𝑛−1
 lines describe the air routes. The 𝑖
-th of them contains two integers 𝑢𝑖
 and 𝑣𝑖
 (1≤𝑢𝑖,𝑣𝑖≤𝑛,𝑢𝑖≠𝑣𝑖
) — the islands connected by the 𝑖
-th air route.

Output
Print a single integer — the expect number of the good islands modulo 109+7
.

Formally, let 𝑀=109+7
. It can be shown that the answer can be expressed as an irreducible fraction 𝑝𝑞
, where 𝑝
 and 𝑞
 are integers and 𝑞≢0
 (mod𝑀
). Output the integer equal to 𝑝⋅𝑞−1
 mod𝑀
. In other words, output such an integer 𝑥
 that 0≤𝑥<𝑀
 and 𝑥⋅𝑞≡𝑝
 (mod𝑀
).
'''
'''
Sample Input:
4 2
1 2
2 3
3 4
Sample Output:
666666674
'''
import sys
from collections import deque

input = sys.stdin.readline
#rounds = int(input())
for ii in range(1):
  out=0
  mod=10**9+7
  island,ppl=map(int,input().split())
  edge={}
  cnt={}
  tree={}
  for p in range(1,island+1):
    edge[p]=[]
    cnt[p]=0
    tree[p]=1
    
  for e in range(island-1):
    n1,n2=map(int,input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)
    cnt[n1]+=1
    cnt[n2]+=1
  if ppl==1 or ppl==3:
    print(1)
    continue
  queue=deque()
  for c in cnt:
    if cnt[c]==1:
      queue.append(c)
  visited=set()
  
  while queue:
    cur=queue.popleft()
    visited.add(cur)
    for e in edge[cur]:
      cnt[e]-=1
      if e not in visited:
        if cnt[e]==1:
          queue.append(e)
        tree[e]+=tree[cur]
        out+=(tree[cur]*(island-tree[cur]))
        out%=mod
  total=(island*(island-1))//2
  out+=(total)
  out%=mod
  print(pow(total,-1,mod)*out%mod)
      
      
