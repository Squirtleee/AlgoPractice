# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
'''Question:https://codeforces.com/contest/1720/problem/D1
You are given an array of 𝑛 integers 𝑎0,𝑎1,𝑎2,…𝑎𝑛−1. Bryap wants to find the longest beautiful subsequence in the array.

An array 𝑏=[𝑏0,𝑏1,…,𝑏𝑚−1], where 0≤𝑏0<𝑏1<…<𝑏𝑚−1<𝑛, is a subsequence of length 𝑚 of the array 𝑎.

Subsequence 𝑏=[𝑏0,𝑏1,…,𝑏𝑚−1] of length 𝑚 is called beautiful, if the following condition holds:

For any 𝑝 (0≤𝑝<𝑚−1) holds: 𝑎𝑏𝑝⊕𝑏𝑝+1<𝑎𝑏𝑝+1⊕𝑏𝑝.
Here 𝑎⊕𝑏 denotes the bitwise XOR of 𝑎 and 𝑏. For example, 2⊕4=6 and 3⊕1=2.

Bryap is a simple person so he only wants to know the length of the longest such subsequence. Help Bryap and find the answer to his question.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤105)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer 𝑛 (2≤𝑛≤3⋅105) — the length of the array.

The second line of each test case contains 𝑛 integers 𝑎0,𝑎1,...,𝑎𝑛−1 (0≤𝑎𝑖≤200) — the elements of the array.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 3⋅105.

Output
For each test case print a single integer — the length of the longest beautiful subsequence.
'''
'''
Sample Input:
3
2
1 2
5
5 2 4 3 1
10
3 8 8 2 9 1 6 2 8 3
Sample Output:
2
3
6
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  arr=list(map(int,input().split()))
  dp=[0]*length
  for l in range(length):
    big_ind=l
    for b in range(l-1,max(-1,l-257),-1):
      small_ind=b
      if arr[small_ind]^big_ind<arr[big_ind]^small_ind:
        dp[l]=max(dp[l],dp[small_ind]+1)
  print(max(dp)+1)
