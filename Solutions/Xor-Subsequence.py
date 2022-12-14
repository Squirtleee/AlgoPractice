# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1720/submission/169154692
'''
Question Link: https://codeforces.com/contest/1720/problem/D1

You are given an array of ๐ integers ๐0,๐1,๐2,โฆ๐๐โ1. Bryap wants to find the longest beautiful subsequence in the array.

An array ๐=[๐0,๐1,โฆ,๐๐โ1], where 0โค๐0<๐1<โฆ<๐๐โ1<๐, is a subsequence of length ๐ of the array ๐.

Subsequence ๐=[๐0,๐1,โฆ,๐๐โ1] of length ๐ is called beautiful, if the following condition holds:

For any ๐ (0โค๐<๐โ1) holds: ๐๐๐โ๐๐+1<๐๐๐+1โ๐๐.
Here ๐โ๐ denotes the bitwise XOR of ๐ and ๐. For example, 2โ4=6 and 3โ1=2.

Bryap is a simple person so he only wants to know the length of the longest such subsequence. Help Bryap and find the answer to his question.

Input
The first line contains a single integer ๐ก (1โค๐กโค105)  โ the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer ๐ (2โค๐โค3โ105) โ the length of the array.

The second line of each test case contains ๐ integers ๐0,๐1,...,๐๐โ1 (0โค๐๐โค200) โ the elements of the array.

It is guaranteed that the sum of ๐ over all test cases does not exceed 3โ105.

Output
For each test case print a single integer โ the length of the longest beautiful subsequence.
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
