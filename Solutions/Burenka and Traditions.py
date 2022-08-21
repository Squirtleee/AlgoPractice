# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1719/submission/168719628
'''
Question Link: https://codeforces.com/contest/1719/problem/D1

Burenka is the crown princess of Buryatia, and soon she will become the 𝑛-th queen of the country. There is an ancient tradition in Buryatia — before the coronation, the ruler must show their strength to the inhabitants. To determine the strength of the 𝑛-th ruler, the inhabitants of the country give them an array of 𝑎 of exactly 𝑛 numbers, after which the ruler must turn all the elements of the array into zeros in the shortest time. The ruler can do the following two-step operation any number of times:

select two indices 𝑙 and 𝑟, so that 1≤𝑙≤𝑟≤𝑛 and a non-negative integer 𝑥, then
for all 𝑙≤𝑖≤𝑟 assign 𝑎𝑖:=𝑎𝑖⊕𝑥, where ⊕ denotes the bitwise XOR operation. It takes ⌈𝑟−𝑙+12⌉ seconds to do this operation, where ⌈𝑦⌉ denotes 𝑦 rounded up to the nearest integer.
Help Burenka calculate how much time she will need.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤5000) — the size of the array.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (0≤𝑎𝑖≤5000) — elements of the array.

It is guaranteed that the sum of 𝑛 in all tests does not exceed 5000.

Output
For each test case, output a single number  — the minimum time that Burenka will need.
'''
'''
Sample Input:
7
4
5 5 5 5
3
1 3 2
2
0 0
3
2 5 7
6
1 2 3 3 2 1
10
27 27 34 32 2 31 23 56 52 4
5
1822 1799 57 23 55
Sample Output:
2
2
0
2
4
7
4
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  out=length
  arr=list(map(int,input().split()))
  num=set()
  num.add(0)
  for a in arr:
    if a in num:
      out-=1
      num=set()
      num.add(0)
    else:
      num2=set()
      for n in num:
        num2.add(n^a)
      num2.add(a)
      num2.add(0)
      num=num2
  print(out)
