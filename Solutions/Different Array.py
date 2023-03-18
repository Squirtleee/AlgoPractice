# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1783/submission/188843123
'''
Quesiton Link: https://codeforces.com/contest/1783/problem/D

You are given an array 𝑎
 consisting of 𝑛
 integers.

You have to perform the sequence of 𝑛−2
 operations on this array:

during the first operation, you either add 𝑎2
 to 𝑎1
 and subtract 𝑎2
 from 𝑎3
, or add 𝑎2
 to 𝑎3
 and subtract 𝑎2
 from 𝑎1
;
during the second operation, you either add 𝑎3
 to 𝑎2
 and subtract 𝑎3
 from 𝑎4
, or add 𝑎3
 to 𝑎4
 and subtract 𝑎3
 from 𝑎2
;
...
during the last operation, you either add 𝑎𝑛−1
 to 𝑎𝑛−2
 and subtract 𝑎𝑛−1
 from 𝑎𝑛
, or add 𝑎𝑛−1
 to 𝑎𝑛
 and subtract 𝑎𝑛−1
 from 𝑎𝑛−2
.
So, during the 𝑖
-th operation, you add the value of 𝑎𝑖+1
 to one of its neighbors, and subtract it from the other neighbor.

For example, if you have the array [1,2,3,4,5]
, one of the possible sequences of operations is:

subtract 2
 from 𝑎3
 and add it to 𝑎1
, so the array becomes [3,2,1,4,5]
;
subtract 1
 from 𝑎2
 and add it to 𝑎4
, so the array becomes [3,1,1,5,5]
;
subtract 5
 from 𝑎3
 and add it to 𝑎5
, so the array becomes [3,1,−4,5,10]
.
So, the resulting array is [3,1,−4,5,10]
.

An array is reachable if it can be obtained by performing the aforementioned sequence of operations on 𝑎
. You have to calculate the number of reachable arrays, and print it modulo 998244353
.

Input
The first line contains one integer 𝑛
 (3≤𝑛≤300
).

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖≤300
).

Output
Print one integer — the number of reachable arrays. Since the answer can be very large, print its remainder modulo 998244353.
'''
'''
Sample Input:
4
1 1 1 1
Sample Output:
3
'''
import sys
input = sys.stdin.readline
#rounds = int(input())
for ii in range(1):
    out=0
    length=int(input())
    arr=list(map(int,input().split()))
    mod=998244353
    dp=[0]*190000
    dp[arr[1]]=1
    for op in range(2,length):
        dp2=[0]*190000
        for j in range(-90000,90001):
            dp2[j+arr[op]]+=dp[j] 
            if j!=0:
                dp2[j-arr[op]]+=dp[j] 
        for s in range(len(dp2)):
            dp2[s]%=mod
        dp=dp2
    print(sum(dp)%mod)
