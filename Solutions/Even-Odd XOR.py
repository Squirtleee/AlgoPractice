# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1722/submission/171760950
'''
Question Link: https://codeforces.com/contest/1722/problem/G

Given an integer 𝑛, find any array 𝑎 of 𝑛 distinct nonnegative integers less than 231 such that the bitwise XOR of the elements on odd indices equals the bitwise XOR of the elements on even indices.

Input
The first line of the input contains an integer 𝑡 (1≤𝑡≤629) — the number of test cases.

Then 𝑡 lines follow, each containing a single integer 𝑛 (3≤𝑛≤2⋅105) — the length of the array.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, output one line containing 𝑛 distinct integers that satisfy the conditions.

If there are multiple answers, you can output any of them.
'''
'''
Sample Input:
7
8
3
4
5
6
7
9

Sample Output:
4 2 1 5 0 6 7 3
2 1 3
2 1 3 0
2 0 4 5 3
4 1 2 12 3 8
1 2 3 4 5 6 7
8 2 3 7 4 0 5 6 9
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  if length%4==0:
    print(2,1,3,0,end=' ')
    for z in range(24,24+length-4):
      print(z,end=' ')
  elif length%4==1:
    print(2,0,4,5,3,end=' ')
    for z in range(24,24+length-5):
      print(z,end=' ')
  elif length%4==2:
    print(4,1,2,12,3,8,end=' ')
    for d in range(24,24+length-6):
      print(d,end=' ')
  else:
    print(2,1,3,end=' ')
    for d in range(24,24+length-3):
      print(d,end=' ')
  print('')
