# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1742/submission/176226883
'''
Question Link: https://codeforces.com/contest/1742/problem/G

You are given an array 𝑎 consisting of 𝑛 nonnegative integers.

Let's define the prefix OR array 𝑏 as the array 𝑏𝑖=𝑎1 𝖮𝖱 𝑎2 𝖮𝖱 … 𝖮𝖱 𝑎𝑖, where 𝖮𝖱 represents the bitwise OR operation. In other words, the array 𝑏 is formed by computing the 𝖮𝖱 of every prefix of 𝑎.

You are asked to rearrange the elements of the array 𝑎 in such a way that its prefix OR array is lexicographically maximum.

An array 𝑥 is lexicographically greater than an array 𝑦 if in the first position where 𝑥 and 𝑦 differ, 𝑥𝑖>𝑦𝑖.

Input
The first line of the input contains a single integer 𝑡 (1≤𝑡≤100) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤2⋅105) — the length of the array 𝑎.

The second line of each test case contains 𝑛 nonnegative integers 𝑎1,…,𝑎𝑛 (0≤𝑎𝑖≤109).

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case print 𝑛 integers — any rearrangement of the array 𝑎 that obtains the lexicographically maximum prefix OR array.
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
