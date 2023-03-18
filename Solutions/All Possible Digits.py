# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1759/submission/193673818
'''
Question Link: https://codeforces.com/contest/1759/problem/F

A positive number 𝑥
 of length 𝑛
 in base 𝑝
 (2≤𝑝≤109
) is written on the blackboard. The number 𝑥
 is given as a sequence 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖<𝑝
) — the digits of 𝑥
 in order from left to right (most significant to least significant).

Dmitry is very fond of all the digits of this number system, so he wants to see each of them at least once.

In one operation, he can:

take any number 𝑥
 written on the board, increase it by 1
, and write the new value 𝑥+1
 on the board.
For example, 𝑝=5
 and 𝑥=2345
.

Initially, the board contains the digits 2
, 3
 and 4
;
Dmitry increases the number 2345
 by 1
 and writes down the number 2405
. On the board there are digits 0,2,3,4
;
Dmitry increases the number 2405
 by 1
 and writes down the number 2415
. Now the board contains all the digits from 0
 to 4
.
Your task is to determine the minimum number of operations required to make all the digits from 0
 to 𝑝−1
 appear on the board at least once.

Input
The first line of the input contains a single integer 𝑡
 (1≤𝑡≤2⋅103
) — the number of test cases. The descriptions of the input test cases follow.

The first line of description of each test case contains two integers 𝑛
 (1≤𝑛≤100
) and 𝑝
 (2≤𝑝≤109
) — the length of the number and the base of the number system.

The second line of the description of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖<𝑝
) — digits of 𝑥
 in number system with base 𝑝
It is guaranteed that the number 𝑥
 does not contain leading zeros (that is, 𝑎1>0
).

Output
For each test case print a single integer — the minimum number of operations required for Dmitry to get all the digits on the board from 0
 to 𝑝−1
.

It can be shown that this always requires a finite number of operations.
'''
'''
Sample Input:
11
2 3
1 2
4 2
1 1 1 1
6 6
1 2 3 4 5 0
5 2
1 0 1 0 1
3 10
1 2 3
5 1000
4 1 3 2 5
3 5
2 3 4
4 4
3 2 3 0
1 3
2
5 5
1 2 2 2 4
3 4
1 0 1
Sample Output:
1
1
0
0
7
995
2
1
1
1
2
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length,base=map(int,input().split())
  digit=list(map(int,input().split()))
  last=digit[-1]
  hv=set(digit)
  while last in hv:
    last-=1
    if last<0:
      last+=base
    if last==digit[-1]:
      break
  if last>=digit[-1]:
    print(last-digit[-1])
  else:
    done=False
    ori=digit[-1]
    digit[-1]=base-1
    for l in range(length-1,-1,-1):
      hv.add((digit[l]+1)%base)
      if (digit[l]+1)!=base:
        break
      if l==0:
        done=True
    if done:
      hv.add(1)
    while last in hv:
      last-=1
      if last==-1:
        break
    if last==-1:
      print(base-ori)
    else:
      print(base-ori+last)

