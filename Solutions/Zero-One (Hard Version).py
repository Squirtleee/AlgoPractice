# Time Limit per Test: 3 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1733/submission/173128808
'''
Question Link: https://codeforces.com/contest/1733/problem/D2

You are given two binary strings 𝑎 and 𝑏, both of length 𝑛. You can do the following operation any number of times (possibly zero).

Select two indices 𝑙 and 𝑟 (𝑙<𝑟).
Change 𝑎𝑙 to (1−𝑎𝑙), and 𝑎𝑟 to (1−𝑎𝑟).
If 𝑙+1=𝑟, the cost of the operation is 𝑥. Otherwise, the cost is 𝑦.
You have to find the minimum cost needed to make 𝑎 equal to 𝑏 or say there is no way to do so.

Input
The first line contains one integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

Each test case consists of three lines. The first line of each test case contains three integers 𝑛, 𝑥, and 𝑦 (5≤𝑛≤5000, 1≤𝑥,𝑦≤109) — the length of the strings, and the costs per operation.

The second line of each test case contains the string 𝑎 of length 𝑛. The string only consists of digits 0 and 1.

The third line of each test case contains the string 𝑏 of length 𝑛. The string only consists of digits 0 and 1.

It is guaranteed that the sum of 𝑛 over all test cases doesn't exceed 5000.

Output
For each test case, if there is no way to make 𝑎 equal to 𝑏, print −1. Otherwise, print the minimum cost needed to make 𝑎 equal to 𝑏.
'''
'''
Sample Input:
6
5 8 9
01001
00101
6 2 11
000001
100000
5 7 2
01000
11011
7 8 3
0111001
0100001
6 3 4
010001
101000
5 10 1
01100
01100

Sample Output:
8
10
-1
6
7
0
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length,x,y=map(int,input().split())
  arr1=input()
  arr2=input()
  arr1=[a for a in arr1]
  arr2=[b for b in arr2]
  arr1.pop()
  arr2.pop()
  diff=0
  change=[]
  for l in range(length):
    if arr1[l]!=arr2[l]:
      diff+=1
      change.append(l)
  if diff%2==1:
    out=-1
  if x>=y and out==0:
      if diff>2:
        out+=(y*diff//2)
      elif diff>0:
        if change[0]+1==change[1]:
          out+=(min(x,y*2))
        else:
          out+=y
  elif out==0:
    dp=[0]*diff
    for ind in range(diff):
      if ind==0:
        continue
      elif ind==1:
        dp[1]=min(y,(change[1]-change[0])*x)
      elif (ind+1)%2==1:
        dp[ind]=min(dp[ind-1],dp[ind-2]+(x*(change[ind]-change[ind-1])))
      else:
        dp[ind]=min(dp[ind-1]+y,dp[ind-2]+(x*(change[ind]-change[ind-1])))
    if diff==0:
      out=0
    else:
      out=dp[-1]
        
  print(out)
