# Time Limit per Test: 3 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1795/submission/195399945
'''
Question Link: https://codeforces.com/contest/1795/problem/D

You are given an undirected graph consisting of 𝑛
 vertices and 𝑛
 edges, where 𝑛
 is divisible by 6
. Each edge has a weight, which is a positive (greater than zero) integer.

The graph has the following structure: it is split into 𝑛3
 triples of vertices, the first triple consisting of vertices 1,2,3
, the second triple consisting of vertices 4,5,6
, and so on. Every pair of vertices from the same triple is connected by an edge. There are no edges between vertices from different triples.

You have to paint the vertices of this graph into two colors, red and blue. Each vertex should have exactly one color, there should be exactly 𝑛2
 red vertices and 𝑛2
 blue vertices. The coloring is called valid if it meets these constraints.

The weight of the coloring is the sum of weights of edges connecting two vertices with different colors.

Let 𝑊
 be the maximum possible weight of a valid coloring. Calculate the number of valid colorings with weight 𝑊
, and print it modulo 998244353
.

Input
The first line contains one integer 𝑛
 (6≤𝑛≤3⋅105
, 𝑛
 is divisible by 6
).

The second line contains 𝑛
 integers 𝑤1,𝑤2,…,𝑤𝑛
 (1≤𝑤𝑖≤1000
) — the weights of the edges. Edge 1
 connects vertices 1
 and 2
, edge 2
 connects vertices 1
 and 3
, edge 3
 connects vertices 2
 and 3
, edge 4
 connects vertices 4
 and 5
, edge 5
 connects vertices 4
 and 6
, edge 6
 connects vertices 5
 and 6
, and so on.

Output
Print one integer — the number of valid colorings with maximum possible weight, taken modulo 998244353
.
'''
'''
Sample Input:
12
1 3 3 7 8 5 2 2 2 2 4 2
Sample Output:
36
'''
import sys
input = sys.stdin.readline
#rounds = int(input())

MOD = 998244353 #look out
nmax = 10**5+1 #look out
fact = [1] * (nmax+1)
for i in range(2, nmax+1):
    fact[i] = fact[i-1] * i % MOD
inv = [1] * (nmax+1)
inv[nmax] = pow(fact[nmax], MOD-2, MOD)
for i in range(nmax-1, 0, -1):
    inv[i] = inv[i+1] * (i+1) % MOD
 
def C(n, m):
    return fact[n] * inv[m] % MOD * inv[n-m] % MOD if 0 <= m <= n else 0


for ii in range(1):
  out=0
  mod=998244353
  length=int(input())
  edge=list(map(int,input().split())) #1 to 2, 1 to 3, 2 to 3...
  cur=(C(length//3,length//6))
  cur%=mod
  two=0
  three=0
  for g in range(0,length,3):
    v1=edge[g]
    v2=edge[g+1]
    v3=edge[g+2]
    if v1!=v2 and v1!=v3 and v2!=v3:
      continue
    elif v1==v2==v3:
      three+=1
    else:
      small=min(v1,v2,v3)
      if small==v1 and small==v2:
        two+=1
      elif small==v1 and small==v3:
        two+=1
      elif small==v2 and small==v3:
        two+=1
  time1=pow(2,two,mod)
  time2=pow(3,three,mod)
  cur=cur*time1*time2%mod
  print(cur)



