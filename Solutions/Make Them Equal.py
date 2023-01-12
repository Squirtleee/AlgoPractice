# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1633/submission/188399555
'''
Question Link: https://codeforces.com/contest/1633/problem/D

You have an array of integers 𝑎 of size 𝑛. Initially, all elements of the array are equal to 1. You can perform the following operation: choose two integers 𝑖 (1≤𝑖≤𝑛) and 𝑥 (𝑥>0), and then increase the value of 𝑎𝑖 by ⌊𝑎𝑖𝑥⌋ (i.e. make 𝑎𝑖=𝑎𝑖+⌊𝑎𝑖𝑥⌋).

After performing all operations, you will receive 𝑐𝑖 coins for all such 𝑖 that 𝑎𝑖=𝑏𝑖.

Your task is to determine the maximum number of coins that you can receive by performing no more than 𝑘 operations.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤100) — the number of test cases.

The first line of each test case contains two integers 𝑛 and 𝑘 (1≤𝑛≤103;0≤𝑘≤106) — the size of the array and the maximum number of operations, respectively.

The second line contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (1≤𝑏𝑖≤103).

The third line contains 𝑛 integers 𝑐1,𝑐2,…,𝑐𝑛 (1≤𝑐𝑖≤106).

The sum of 𝑛 over all test cases does not exceed 103.

Output
For each test case, print one integer — the maximum number of coins that you can get by performing no more than 𝑘 operations.
'''
'''
Sample Input:
4
4 4
1 7 5 2
2 6 5 2
3 0
3 5 2
5 4 7
5 9
5 2 5 6 3
5 9 1 9 7
6 14
11 4 6 2 8 16
43 45 9 41 15 38
Sample Output:
9
0
30
167
'''
import sys
input = sys.stdin.readline

times=[100000]*1001
times[0]=0
times[1]=0
for n in range(1,1001):
  for x in range(1,n+1):
    if n+n//x<1001:
      times[n+n//x]=min(times[n+n//x],1+times[n])


def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Making the dp array
 
    for i in range(1, n+1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
                                # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
 
    return dp[W]


rounds = int(input())
for ii in range(rounds):
  out=0
  length,ope=map(int,input().split())
  ope=min(ope,max(times)*1001)
  goal=list(map(int,input().split()))
  coin=list(map(int,input().split()))
  weight=[]
  val=[]
  for l in range(length):
    if goal[l]==1:
      out+=coin[l]
    else:
      weight.append(times[goal[l]])
      val.append(coin[l])
    
    
      
  print (knapSack(ope,weight,val,len(weight))+out)
