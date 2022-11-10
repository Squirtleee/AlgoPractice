# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1750/submission/180256907
'''
Question Link: https://codeforces.com/contest/1750/problem/D

You are given two integers 𝑛 and 𝑚 and an array 𝑎 of 𝑛 integers. For each 1≤𝑖≤𝑛 it holds that 1≤𝑎𝑖≤𝑚.

Your task is to count the number of different arrays 𝑏 of length 𝑛 such that:

1≤𝑏𝑖≤𝑚 for each 1≤𝑖≤𝑛, and
gcd(𝑏1,𝑏2,𝑏3,...,𝑏𝑖)=𝑎𝑖 for each 1≤𝑖≤𝑛.
Here gcd(𝑎1,𝑎2,…,𝑎𝑖) denotes the greatest common divisor (GCD) of integers 𝑎1,𝑎2,…,𝑎𝑖.

Since this number can be too large, print it modulo 998244353.

Input
Each test consist of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤100) — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 (1≤𝑛≤2⋅105, 1≤𝑚≤109) — the length of the array 𝑎 and the maximum possible value of the element.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑚) — the elements of the array 𝑎.

It is guaranteed that the sum of 𝑛 across all test cases doesn't exceed 2⋅105.

Output
For each test case, print a single integer — the number of different arrays satisfying the conditions above. Since this number can be large, print it modulo 998244353.
'''
'''
Sample Input:
5
3 5
4 2 1
2 1
1 1
5 50
2 3 5 2 3
4 1000000000
60 30 1 1
2 1000000000
1000000000 2

Sample Output:
3
1
0
595458194
200000000
'''
import sys
from itertools import combinations
input = sys.stdin.readline
rounds = int(input())

def isPrime(number):
  for t in range(2,int(number**0.5)+1):
    if number%t==0:
      return False
  return True

for ii in range(rounds):
  out=0
  mod=998244353 
  length,big=map(int,input().split())
  arr=list(map(int,input().split()))
  ans=1
  for l in range(1,length):
    if arr[l]>arr[l-1] or arr[l-1]%arr[l]!=0:
      ans=0
      break
    if arr[l]==arr[l-1]:
      ans*=(big//arr[l])
      ans%=mod
    else:
      cnt=big//arr[l]
      useless=arr[l-1]//arr[l]
      nopeFactor=set()
      o=2
      while o*o<=useless:
        if useless%o==0 and isPrime(o):
          nopeFactor.add(o)
          while useless%o==0:
            useless//=o
        o+=1
      if useless!=1:
        nopeFactor.add(useless)
      #for u in range(2,useless+1):
      #  if useless%u==0 and isPrime(u):
      #    nopeFactor.add(u)
      #print(nopeFactor)
      for c in range(1,len(nopeFactor)+1):
        coll=combinations(list(nopeFactor),c)
        for co in coll:
          multi=1
          for k in co:
            multi*=k
          if c%2==1:
            cnt-=(big//arr[l]//multi)
          else:
            cnt+=(big//arr[l]//multi)
      ans*=cnt
      ans%=mod
  print(ans%mod)
