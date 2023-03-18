# Time Limit per Test: 4 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1782/submission/189789224
'''
Quesiton Link: https://codeforces.com/contest/1782/problem/D

You are given a set 𝑎1,𝑎2,…,𝑎𝑛
 of distinct positive integers.

We define the squareness of an integer 𝑥
 as the number of perfect squares among the numbers 𝑎1+𝑥,𝑎2+𝑥,…,𝑎𝑛+𝑥
.

Find the maximum squareness among all integers 𝑥
 between 0
 and 1018
, inclusive.

Perfect squares are integers of the form 𝑡2
, where 𝑡
 is a non-negative integer. The smallest perfect squares are 0,1,4,9,16,…
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤50
). The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤50
) — the size of the set.

The second line contains 𝑛
 distinct integers 𝑎1,𝑎2,…,𝑎𝑛
 in increasing order (1≤𝑎1<𝑎2<…<𝑎𝑛≤109
) — the set itself.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 50
.

Output
For each test case, print a single integer — the largest possible number of perfect squares among 𝑎1+𝑥,𝑎2+𝑥,…,𝑎𝑛+𝑥
, for some 0≤𝑥≤1018.
'''
'''
Sample Input:
4
5
1 2 3 4 5
5
1 6 13 22 97
1
100
5
2 5 10 17 26
Sample Output:
2
5
1
2
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=1
  length=int(input())
  arr=list(map(int,input().split()))
  cnt={}
  for i in range(length-1):
    for j in range(i+1,length):
      if arr[j]<arr[i]:
        continue
      diff=arr[j]-arr[i]
      div=[]
      for d in range(1,int(diff**0.5)+1):
        if diff%d==0:
          div.append(d)
      for d in div:
        if (d+(diff//d))%2==0:
          m=(d+(diff//d))//2
          x=m**2-arr[j]
          if x>=0:
            if x not in cnt:
              cnt[x]=set()
            cnt[x].add(arr[i])
            cnt[x].add(arr[j])
  for c in cnt:
    out=max(out,len(cnt[c]))
  print(out)
