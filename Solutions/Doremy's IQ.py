# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1708/submission/164529005
'''
Question Link: https://codeforces.com/contest/1708/problem/C

Doremy is asked to test ๐ contests. Contest ๐ can only be tested on day ๐. The difficulty of contest ๐ is ๐๐. Initially, Doremy's IQ is ๐. On day ๐ Doremy will choose whether to test contest ๐ or not. She can only test a contest if her current IQ is strictly greater than 0.

If Doremy chooses to test contest ๐ on day ๐, the following happens:

if ๐๐>๐, Doremy will feel she is not wise enough, so ๐ decreases by 1;
otherwise, nothing changes.
If she chooses not to test a contest, nothing changes.
Doremy wants to test as many contests as possible. Please give Doremy a solution.

Input
The input consists of multiple test cases. The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of test cases. The description of the test cases follows.

The first line contains two integers ๐ and ๐ (1โค๐โค105, 1โค๐โค109) โ the number of contests and Doremy's IQ in the beginning.

The second line contains ๐ integers ๐1,๐2,โฏ,๐๐ (1โค๐๐โค109) โ the difficulty of each contest.

It is guaranteed that the sum of ๐ over all test cases does not exceed 105.

Output
For each test case, you need to output a binary string ๐ , where ๐ ๐=1 if Doremy should choose to test contest ๐, and ๐ ๐=0 otherwise. The number of ones in the string should be maximum possible, and she should never test a contest when her IQ is zero or less.

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
