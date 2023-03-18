# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1778/submission/192073114
'''
Question Link: https://codeforces.com/contest/1778/problem/D

You are given two binary strings 𝑎
 and 𝑏
 of length 𝑛
. In each move, the string 𝑎
 is modified in the following way.

An index 𝑖
 (1≤𝑖≤𝑛
) is chosen uniformly at random. The character 𝑎𝑖
 will be flipped. That is, if 𝑎𝑖
 is 0
, it becomes 1
, and if 𝑎𝑖
 is 1
, it becomes 0
.
What is the expected number of moves required to make both strings equal for the first time?

A binary string is a string, in which the character is either 𝟶
 or 𝟷
.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤105
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤106
) — the length of the strings.

The second line of each test case contains the binary string 𝑎
 of length 𝑛
.

The third line of each test case contains the binary string 𝑏
 of length 𝑛
.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 106
.

Output
For each test case, output a single line containing the expected number of moves modulo 998244353
.

Formally, let 𝑀=998244353
. It can be shown that the answer can be expressed as an irreducible fraction 𝑝𝑞
, where 𝑝
 and 𝑞
 are integers and 𝑞≢0(mod𝑀)
. Output the integer equal to 𝑝⋅𝑞−1mod𝑀
. In other words, output such an integer 𝑥
 that 0≤𝑥<𝑀
 and 𝑥⋅𝑞≡𝑝(mod𝑀)
.
'''
'''
Sample Input:
4
1
0
1
2
00
00
4
1000
1110
5
01001
10111
Sample Output:
1
0
665496254
665496277
'''

import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  cur=input()
  goal=input()
  mod=998244353
  diff=[0]*(length+1)
  diff[-1]=1
  for l in range(length-1,0,-1):
    diff[l]=((length)*pow(l,-1,mod)+((length-l))*pow(l,-1,mod)*(diff[l+1]))%mod
  for l in range(length):
    if cur[l]!=goal[l]:
      out+=1
  ans=0
  for t in range(out+1):
    ans+=diff[t]
  print(ans%mod)
