# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1716/submission/167112457
'''
Question Link: https://codeforces.com/contest/1716/problem/D

There is a chip on the coordinate line. Initially, the chip is located at the point 0. You can perform any number of moves; each move increases the coordinate of the chip by some positive integer (which is called the length of the move). The length of the first move you make should be divisible by 𝑘, the length of the second move — by 𝑘+1, the third — by 𝑘+2, and so on.

For example, if 𝑘=2, then the sequence of moves may look like this: 0→4→7→19→44, because 4−0=4 is divisible by 2=𝑘, 7−4=3 is divisible by 3=𝑘+1, 19−7=12 is divisible by 4=𝑘+2, 44−19=25 is divisible by 5=𝑘+3.

You are given two positive integers 𝑛 and 𝑘. Your task is to count the number of ways to reach the point 𝑥, starting from 0, for every 𝑥∈[1,𝑛]. The number of ways can be very large, so print it modulo 998244353. Two ways are considered different if they differ as sets of visited positions.

Input
The first (and only) line of the input contains two integers 𝑛 and 𝑘 (1≤𝑘≤𝑛≤2⋅105).

Output
Print 𝑛 integers — the number of ways to reach the point 𝑥, starting from 0, for every 𝑥∈[1,𝑛], taken modulo 998244353.
'''
'''
Sample Input:
8 1
Sample Output:
1 1 2 2 3 4 5 6 
'''
import sys
input = sys.stdin.readline
for ii in range(1):
  out = 0
  length,k=map(int,input().split())
  mod=998244353 
  ans=[0]*(length+1)
  row1=[0]*(length+1)
  row1[0]=1
  

  pos=0
  for j in range(k,length+1):
    pos+=j
    if pos>length:
      break
    cur=[0]*(length+1)
    for p in range(j,length+1):
      cur[p]=(row1[p-j]+cur[p-j])%mod
      ans[p]+=cur[p]
      ans[p]%=mod
    row1=cur
  for y in range(1,length+1):
    print(ans[y],end=' ')
  print('')
