# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1792/submission/190590692
'''
Quesiton Link: https://codeforces.com/contest/1792/problem/D

You are given 𝑛
 permutations 𝑎1,𝑎2,…,𝑎𝑛
, each of length 𝑚
. Recall that a permutation of length 𝑚
 is a sequence of 𝑚
 distinct integers from 1
 to 𝑚
.

Let the beauty of a permutation 𝑝1,𝑝2,…,𝑝𝑚
 be the largest 𝑘
 such that 𝑝1=1,𝑝2=2,…,𝑝𝑘=𝑘
. If 𝑝1≠1
, then the beauty is 0
.

The product of two permutations 𝑝⋅𝑞
 is a permutation 𝑟
 such that 𝑟𝑗=𝑞𝑝𝑗
.

For each 𝑖
 from 1
 to 𝑛
, print the largest beauty of a permutation 𝑎𝑖⋅𝑎𝑗
 over all 𝑗
 from 1
 to 𝑛
 (possibly, 𝑖=𝑗
).

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of testcases.

The first line of each testcase contains two integers 𝑛
 and 𝑚
 (1≤𝑛≤5⋅104
; 1≤𝑚≤10
) — the number of permutations and the length of each permutation.

The 𝑖
-th of the next 𝑛
 lines contains a permutation 𝑎𝑖
 — 𝑚
 distinct integers from 1
 to 𝑚
.

The sum of 𝑛
 doesn't exceed 5⋅104
 over all testcases.

Output
For each testcase, print 𝑛
 integers. The 𝑖
-th value should be equal to the largest beauty of a permutation 𝑎𝑖⋅𝑎𝑗
 over all 𝑗
 (1≤𝑗≤𝑛
).

'''
'''
Sample Input:
3
3 4
2 4 1 3
1 2 4 3
2 1 3 4
2 2
1 2
2 1
8 10
3 4 9 6 10 2 7 8 1 5
3 9 1 8 5 7 4 10 2 6
3 10 1 7 5 9 6 4 2 8
1 2 3 4 8 6 10 7 9 5
1 2 3 4 10 6 8 5 7 9
9 6 1 2 10 4 7 8 3 5
7 9 3 2 5 6 4 8 1 10
9 4 3 7 5 6 1 10 8 2
Sample Output:
1 4 4 
2 2 
10 8 1 6 8 10 1 7 
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  per,length=map(int,input().split())
  total=[]
  aa=[]
  inv=set()
  
  for p in range(per):
    arr=list(map(int,input().split()))
    total.append(arr)
  for j in range(per):
      pre2=[-1]*(length+1)
      for y in range(length):
        pre2[total[j][y]]=y
      seg=[]
      for q in range(1,len(pre2)):
        seg.append(pre2[q])
        inv.add(tuple(seg))
  for i in range(per):
    pre=[-1]*(length+1)
    ans=0
    for l in range(length):
      pre[l+1]=total[i][l]-1 # 1 is at index 0, 2 is at index 4... 
      for c in range(1,length+1):
        cur=tuple(pre[1:c+1])
        if cur in inv:
          ans=max(ans,c)
        else:
          break
    print(ans,end=' ')
  print('')

