# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1646/submission/162506405
'''
Question Link: https://codeforces.com/contest/1646/problem/C

A number is called powerful if it is a power of two or a factorial. In other words, the number 𝑚 is powerful if there exists a non-negative integer 𝑑 such that 𝑚=2𝑑 or 𝑚=𝑑!, where 𝑑!=1⋅2⋅…⋅𝑑 (in particular, 0!=1). For example 1, 4, and 6 are powerful numbers, because 1=1!, 4=22, and 6=3! but 7, 10, or 18 are not.

You are given a positive integer 𝑛. Find the minimum number 𝑘 such that 𝑛 can be represented as the sum of 𝑘 distinct powerful numbers, or say that there is no such 𝑘.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤100). Description of the test cases follows.

A test case consists of only one line, containing one integer 𝑛 (1≤𝑛≤1012).

Output
For each test case print the answer on a separate line.

If 𝑛 can not be represented as the sum of distinct powerful numbers, print −1.

Otherwise, print a single positive integer  — the minimum possible value of 𝑘.
'''
'''
Sample Input:
4
7
11
240
17179869184
Sample Output:
2
3
4
1
'''
factorials=[1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200]

power2=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776]

import sys
from itertools import combinations
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=10**100
  num=int(input())
  base=[]
  for a in range(14):
    if factorials[a]<=num:
      base.append(a)
  
  for p in range(15):
    pos=combinations(base,p)
    for t in pos:
      fact=t
      totalf=0
      cnt=0
      for z in range(len(fact)):
        totalf+=factorials[fact[z]]
        if totalf>num:
          break
        cnt+=1
      if totalf<=num:
        need=num-totalf
        while need>0:
          for x in range(len(power2)-1,-1,-1):
            if power2[x]<=need and power2[x+1]>need:
              need-=power2[x]
              cnt+=1
          if cnt>out:
            break
        if cnt<out:
          out=cnt
  print(out)
