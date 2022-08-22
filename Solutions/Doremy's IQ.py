# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1708/submission/164529005
'''
Question Link: https://codeforces.com/contest/1708/problem/C

Doremy is asked to test 𝑛 contests. Contest 𝑖 can only be tested on day 𝑖. The difficulty of contest 𝑖 is 𝑎𝑖. Initially, Doremy's IQ is 𝑞. On day 𝑖 Doremy will choose whether to test contest 𝑖 or not. She can only test a contest if her current IQ is strictly greater than 0.

If Doremy chooses to test contest 𝑖 on day 𝑖, the following happens:

if 𝑎𝑖>𝑞, Doremy will feel she is not wise enough, so 𝑞 decreases by 1;
otherwise, nothing changes.
If she chooses not to test a contest, nothing changes.
Doremy wants to test as many contests as possible. Please give Doremy a solution.

Input
The input consists of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases. The description of the test cases follows.

The first line contains two integers 𝑛 and 𝑞 (1≤𝑛≤105, 1≤𝑞≤109) — the number of contests and Doremy's IQ in the beginning.

The second line contains 𝑛 integers 𝑎1,𝑎2,⋯,𝑎𝑛 (1≤𝑎𝑖≤109) — the difficulty of each contest.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
For each test case, you need to output a binary string 𝑠, where 𝑠𝑖=1 if Doremy should choose to test contest 𝑖, and 𝑠𝑖=0 otherwise. The number of ones in the string should be maximum possible, and she should never test a contest when her IQ is zero or less.

If there are multiple solutions, you may output any.
'''
'''
Sample Input:
5
1 1
1
2 1
1 2
3 1
1 2 1
4 2
1 4 3 1
5 2
5 1 2 4 3
Sample Output:
1
11
110
1110
01111
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  length,iq=map(int,input().split())
  out=['0']*length
  contest=list(map(int,input().split()))
  bigger=0
  for c in contest:
    if c>iq:
      bigger+=1
  left=0
  r=bigger
  total=0
  while left<r:
    skip=(left+r)//2
    s2=skip
    total=0
    iq2=iq
    for l in range(length):
      if contest[l]<=iq2:
        total+=1
      else:
        if s2>0:
          s2-=1
        else:
          iq2-=1
          total+=1
      if iq2<0:
        break
    if iq2<0:
      left=skip+1
    else:
      r=skip

  nope=left

  for ll in range(length):
    if contest[ll]<=iq:
      out[ll]='1'
    else:
      if nope>0:
        nope-=1
      else:
        out[ll]='1'
  print(''.join(out))
