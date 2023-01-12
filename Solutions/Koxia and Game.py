# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1770/submission/187673598
'''
Question Link: https://codeforces.com/contest/1770/problem/D

Koxia and Mahiru are playing a game with three arrays 𝑎, 𝑏, and 𝑐 of length 𝑛. Each element of 𝑎, 𝑏 and 𝑐 is an integer between 1 and 𝑛 inclusive.

The game consists of 𝑛 rounds. In the 𝑖-th round, they perform the following moves:

Let 𝑆 be the multiset {𝑎𝑖,𝑏𝑖,𝑐𝑖}.
Koxia removes one element from the multiset 𝑆 by her choice.
Mahiru chooses one integer from the two remaining in the multiset 𝑆.
Let 𝑑𝑖 be the integer Mahiru chose in the 𝑖-th round. If 𝑑 is a permutation†, Koxia wins. Otherwise, Mahiru wins.

Currently, only the arrays 𝑎 and 𝑏 have been chosen. As an avid supporter of Koxia, you want to choose an array 𝑐 such that Koxia will win. Count the number of such 𝑐, modulo 998244353.

Note that Koxia and Mahiru both play optimally.

† A permutation of length 𝑛 is an array consisting of 𝑛 distinct integers from 1 to 𝑛 in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (𝑛=3 but there is 4 in the array).

Input
Each test consists of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤2⋅104) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤105) — the size of the arrays.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛).

The third line of each test case contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (1≤𝑏𝑖≤𝑛).

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
Output a single integer — the number of 𝑐 makes Koxia win, modulo 998244353.
'''
'''
Sample Input:
2
3
1 2 2
1 3 3
5
3 3 1 3 4
4 5 2 5 5
Sample Output:
6
0
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=1
  length=int(input())
  arr1=list(map(int,input().split()))
  arr2=list(map(int,input().split()))
  mod=998244353
  edge={}
  for l in range(length):
    edge[l+1]=[]
  selfL=0
  self=set()
  for l in range(length):
      edge[arr1[l]].append(arr2[l])
      edge[arr2[l]].append(arr1[l])
  #dfs for counting Vertex=Edge component
  visited=set()
  stack=[]
  comp=0
  v=1
  while len(visited)<length-len(self):
    while v in self or v in visited:
      v+=1
    stack.append(v)
    cnte=0
    cntv=0
    selfL=0
    while stack:
      cur=stack.pop()
      if cur in visited or cur in self:
        continue
      cntv+=1
      visited.add(cur)
      for e in (edge[cur]):
        if e==cur:
          selfL+=1
        stack.append(e)
        cnte+=1
    #print(selfL,cntv,cnte)
    if selfL>0:
      out*=length
      out%=mod    
    elif cnte==2*cntv:
      out*=2
      out%=mod
    else:
      out=0
    
    
  print(out)
