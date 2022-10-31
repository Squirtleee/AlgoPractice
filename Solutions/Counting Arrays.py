# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1749/submission/177505199
'''
Question Link: https://codeforces.com/contest/1749/problem/D

Consider an array 𝑎 of length 𝑛 with elements numbered from 1 to 𝑛. It is possible to remove the 𝑖-th element of 𝑎 if 𝑔𝑐𝑑(𝑎𝑖,𝑖)=1, where 𝑔𝑐𝑑 denotes the greatest common divisor. After an element is removed, the elements to the right are shifted to the left by one position.

An array 𝑏 with 𝑛 integers such that 1≤𝑏𝑖≤𝑛−𝑖+1 is a removal sequence for the array 𝑎 if it is possible to remove all elements of 𝑎, if you remove the 𝑏1-th element, then the 𝑏2-th, ..., then the 𝑏𝑛-th element. For example, let 𝑎=[42,314]:

[1,1] is a removal sequence: when you remove the 1-st element of the array, the condition 𝑔𝑐𝑑(42,1)=1 holds, and the array becomes [314]; when you remove the 1-st element again, the condition 𝑔𝑐𝑑(314,1)=1 holds, and the array becomes empty.
[2,1] is not a removal sequence: when you try to remove the 2-nd element, the condition 𝑔𝑐𝑑(314,2)=1 is false.
An array is ambiguous if it has at least two removal sequences. For example, the array [1,2,5] is ambiguous: it has removal sequences [3,1,1] and [1,2,1]. The array [42,314] is not ambiguous: the only removal sequence it has is [1,1].

You are given two integers 𝑛 and 𝑚. You have to calculate the number of ambiguous arrays 𝑎 such that the length of 𝑎 is from 1 to 𝑛 and each 𝑎𝑖 is an integer from 1 to 𝑚.

Input
The only line of the input contains two integers 𝑛 and 𝑚 (2≤𝑛≤3⋅105; 1≤𝑚≤1012).

Output
Print one integer — the number of ambiguous arrays 𝑎 such that the length of 𝑎 is from 1 to 𝑛 and each 𝑎𝑖 is an integer from 1 to 𝑚. Since the answer can be very large, print it modulo 998244353.
'''
'''
Sample Input:
2 3
Sample Output:
6
'''
import sys
from math import pow

def isPrime(n):
  for j in range(2,min(int(pow(n,0.5))+4,n)):
    if n%j==0:
      return False
  return True

input = sys.stdin.readline
#rounds = int(input())
for ii in range(1):
  out=0
  length,big=map(int,input().split())
  total=0
  plus=1
  for cnt in range(1,length+1):
    plus*=big
    plus%=998244353
    total+=plus
    total%=998244353
  nope=1
  divisible=[0]*length
  for l in range(1,length+1):
    if isPrime(l):
      nope*=l
    divisible[l-1]=big//nope
  minus=1
  for d in divisible:
    minus*=d
    minus%=998244353
    total-=minus
    total%=998244353
  
  print(int(total)%998244353)
