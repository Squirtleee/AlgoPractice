# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1699/submission/162846267
'''
Question Link: https://codeforces.com/contest/1699/problem/C

You are given a permutation ๐1,๐2,โฆ,๐๐ of integers from 0 to ๐โ1. Your task is to find how many permutations ๐1,๐2,โฆ,๐๐ are similar to permutation ๐.

Two permutations ๐ and ๐ of size ๐ are considered similar if for all intervals [๐,๐] (1โค๐โค๐โค๐), the following condition is satisfied:
MEX([๐๐,๐๐+1,โฆ,๐๐])=MEX([๐๐,๐๐+1,โฆ,๐๐]),
where the MEX of a collection of integers ๐1,๐2,โฆ,๐๐ is defined as the smallest non-negative integer ๐ฅ which does not occur in collection ๐. For example, MEX([1,2,3,4,5])=0, and MEX([0,1,2,4,5])=3.

Since the total number of such permutations can be very large, you will have to print its remainder modulo 10e9+7.

In this problem, a permutation of size ๐ is an array consisting of ๐ distinct integers from 0 to ๐โ1 in arbitrary order. For example, [1,0,2,4,3] is a permutation, while [0,1,1] is not, since 1 appears twice in the array. [0,1,3] is also not a permutation, since ๐=3 and there is a 3 in the array.

Input
Each test contains multiple test cases. The first line of input contains one integer ๐ก (1โค๐กโค10e4) โ the number of test cases. The following lines contain the descriptions of the test cases.

The first line of each test case contains a single integer ๐ (1โค๐โค105) โ the size of permutation ๐.

The second line of each test case contains ๐ distinct integers ๐1,๐2,โฆ,๐๐ (0โค๐๐<๐) โ the elements of permutation ๐.

It is guaranteed that the sum of ๐ across all test cases does not exceed 10e5.

Output
For each test case, print a single integer, the number of permutations similar to permutation ๐, taken modulo 10e9+7.
'''
'''
Sample Input:
5
5
4 0 3 2 1
1
0
4
0 1 2 3
6
1 2 4 0 5 3
8
1 3 7 2 5 0 6 4
Sample Output:
2
1
1
4
72
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=1
  length=int(input())
  arr=list(map(int,input().split()))
  pos=[0]*length
  for l in range(length):
    pos[arr[l]]=l
  l=pos[0]
  r=pos[0]
  for n in range(1,length):
    if l<=pos[n]<=r:
      out*=(r-l+1-n)
      out=out%(10**9+7)
    elif pos[n]<l:
      l=pos[n]
    else:
      r=pos[n]
  print(out)
