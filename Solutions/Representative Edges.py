# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1616/submission/167604259
'''
Question Link: https://codeforces.com/contest/1616/problem/C

An array 𝑎1,𝑎2,…,𝑎𝑛 is good if and only if for every subsegment 1≤𝑙≤𝑟≤𝑛, the following holds: 𝑎𝑙+𝑎𝑙+1+…+𝑎𝑟=12(𝑎𝑙+𝑎𝑟)⋅(𝑟−𝑙+1).

You are given an array of integers 𝑎1,𝑎2,…,𝑎𝑛. In one operation, you can replace any one element of this array with any real number. Find the minimum number of operations you need to make this array good.

Input
The first line of input contains one integer 𝑡 (1≤𝑡≤100): the number of test cases.

Each of the next 𝑡 lines contains the description of a test case.

In the first line you are given one integer 𝑛 (1≤𝑛≤70): the number of integers in the array.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (−100≤𝑎𝑖≤100): the initial array.

Output
For each test case, print one integer: the minimum number of elements that you need to replace to make the given array good.
'''
'''
Sample Input:
5
4
1 2 3 4
4
1 1 2 2
2
0 -1
6
3 -2 4 -1 -4 0
1
-100
Sample Output:
0
2
0
3
0
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=10**20
  length=int(input())
  arr=list(map(float,input().split()))
  for fixed1 in range(length):
    for fixed2 in range(fixed1,length):
      if fixed2-fixed1>0:
        diff=(arr[fixed2]-arr[fixed1])/(fixed2-fixed1)
      else:
        diff=0
      change=0
      left=fixed1-1
      should_l=arr[fixed1]-diff
      right=fixed2+1
      should_r=arr[fixed2]+diff
      shouldm=arr[fixed1]+diff
      k=fixed1+1
      
      for k in range(fixed1+1,fixed2):
        if fixed1!=fixed2 and (arr[k]-arr[fixed1])/(k-fixed1)!=((arr[fixed2]-arr[fixed1])/(fixed2-fixed1)):
          change+=1
        elif fixed1==fixed2 and (arr[k]-arr[fixed1])/(k-fixed1)!=0:
          change+=1
        if change>out:
          break
        
      while left>=0:
        if fixed1!=fixed2 and (arr[fixed1]-arr[left])/(fixed1-left)!=((arr[fixed2]-arr[fixed1])/(fixed2-fixed1)):
          change+=1
        elif fixed1==fixed2 and (arr[fixed1]-arr[left])/(fixed1-left)!=0:
          change+=1
        left-=1
        if change>out:
          break
      
      while right<length:
        if fixed1!=fixed2 and (arr[right]-arr[fixed2])/(right-fixed2)!=((arr[fixed2]-arr[fixed1])/(fixed2-fixed1)):
          change+=1
        elif fixed1==fixed2 and (arr[right]-arr[fixed2])/(right-fixed2)!=0:
          change+=1
        right+=1
        if change>out:
          break
        
      out=min(out,change)
  print(out)
