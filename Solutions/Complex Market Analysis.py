# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1609/submission/165084682
'''
Question Link: https://codeforces.com/contest/1609/problem/C

While performing complex market analysis William encountered the following problem:

For a given array ๐ of size ๐ and a natural number ๐, calculate the number of pairs of natural numbers (๐,๐) which satisfy the following conditions:

1โค๐,๐
๐+๐โ๐โค๐.
Product ๐๐โ๐๐+๐โ๐๐+2โ๐โโฆโ๐๐+๐โ๐ is a prime number.
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.

Input
Each test contains multiple test cases. The first line contains the number of test cases ๐ก (1โค๐กโค10000). Description of the test cases follows.

The first line of each test case contains two integers ๐ and ๐ (1โค๐โค๐โค2โ105), the number of items in the array and number ๐, respectively.

The second line contains ๐ integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค106), the contents of the array.

It is guaranteed that the sum of ๐ over all test cases does not exceed 2โ105.

Output
For each test case output the answer in the following format:

Output one line containing the number of pairs of numbers (๐,๐) which satisfy the conditions.
'''
'''
Sample Input:
6
7 3
10 2 1 3 1 19 3
3 2
1 13 1
9 3
2 4 2 1 1 1 1 4 2
3 1
1 1 1
4 1
1 2 1 1
2 2
1 2
Sample Output:
2
0
4
0
5
0
'''
import sys
input = sys.stdin.readline
import math

prime=set()
not_p=set()
def isPrime(n):
    ori=n
    if n in prime:
      return True
    if n in not_p:
      return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            not_p.add(ori)
            return False
    prime.add(ori)
    return True

rounds=int(input())
for ii in range(rounds):
  out=0
  length,e=map(int,input().split())
  arr=list(map(int,input().split()))
  dp1=[0]*(length+e)
  dp_prime=[0]*(length+e)
  for l in range(length-1,-1,-1):
    if arr[l]==1:
      dp1[l]=dp1[l+e]+1
      dp_prime[l]=dp_prime[l+e]
    elif isPrime(arr[l]):
      dp_prime[l]=dp1[l+e]+1

  for t in range(length-e):
    if arr[t]==1:
      out+=dp_prime[t]
    elif dp_prime[t]>0:
      out+=dp1[t+e]
  print(out)
