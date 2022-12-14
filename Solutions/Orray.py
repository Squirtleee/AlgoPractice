# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1742/submission/176226883
'''
Question Link: https://codeforces.com/contest/1742/problem/G

You are given an array ๐ consisting of ๐ nonnegative integers.

Let's define the prefix OR array ๐ as the array ๐๐=๐1 ๐ฎ๐ฑ ๐2 ๐ฎ๐ฑ โฆ ๐ฎ๐ฑ ๐๐, where ๐ฎ๐ฑ represents the bitwise OR operation. In other words, the array ๐ is formed by computing the ๐ฎ๐ฑ of every prefix of ๐.

You are asked to rearrange the elements of the array ๐ in such a way that its prefix OR array is lexicographically maximum.

An array ๐ฅ is lexicographically greater than an array ๐ฆ if in the first position where ๐ฅ and ๐ฆ differ, ๐ฅ๐>๐ฆ๐.

Input
The first line of the input contains a single integer ๐ก (1โค๐กโค100) โ the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer ๐ (1โค๐โค2โ105) โ the length of the array ๐.

The second line of each test case contains ๐ nonnegative integers ๐1,โฆ,๐๐ (0โค๐๐โค109).

It is guaranteed that the sum of ๐ over all test cases does not exceed 2โ105.

Output
For each test case print ๐ integers โ any rearrangement of the array ๐ that obtains the lexicographically maximum prefix OR array.
'''
'''
Sample Input:
5
4
1 2 4 8
7
5 1 2 3 4 5 5
2
1 101
6
2 3 4 2 3 4
8
1 4 2 3 4 5 7 1
Sample Output:
8 4 2 1 
5 2 1 3 4 5 5 
101 1 
4 3 2 2 3 4 
7 1 4 2 3 4 5 1 
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  arr=list(map(int,input().split()))
  #max 30
  num=0
  ans=[]
  for z in range(min(29,length)):
    arr.sort(key=lambda x:x|num)
    new=arr.pop()
    ans.append((new))
    if num==num|new:
      break
    num=num|new
  for n in arr:
    ans.append((n))

    
  print(*(ans))
