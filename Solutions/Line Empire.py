# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1659/submission/162889629
'''
Question Link: https://codeforces.com/contest/1659/problem/C

You are an ambitious king who wants to be the Emperor of The Reals. But to do that, you must first become Emperor of The Integers.

Consider a number axis. The capital of your empire is initially at 0. There are 𝑛 unconquered kingdoms at positions 0<𝑥1<𝑥2<…<𝑥𝑛. You want to conquer all other kingdoms.

There are two actions available to you:

You can change the location of your capital (let its current position be 𝑐1) to any other conquered kingdom (let its position be 𝑐2) at a cost of 𝑎⋅|𝑐1−𝑐2|.
From the current capital (let its current position be 𝑐1) you can conquer an unconquered kingdom (let its position be 𝑐2) at a cost of 𝑏⋅|𝑐1−𝑐2|. You cannot conquer a kingdom if there is an unconquered kingdom between the target and your capital.
Note that you cannot place the capital at a point without a kingdom. In other words, at any point, your capital can only be at 0 or one of 𝑥1,𝑥2,…,𝑥𝑛. Also note that conquering a kingdom does not change the position of your capital.

Find the minimum total cost to conquer all kingdoms. Your capital can be anywhere at the end.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤1000)  — the number of test cases. The description of each test case follows.

The first line of each test case contains 3 integers 𝑛, 𝑎, and 𝑏 (1≤𝑛≤2⋅105; 1≤𝑎,𝑏≤105).

The second line of each test case contains 𝑛 integers 𝑥1,𝑥2,…,𝑥𝑛 (1≤𝑥1<𝑥2<…<𝑥𝑛≤108).

The sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, output a single integer  — the minimum cost to conquer all kingdoms.
'''
'''
Sample Input:
4
5 2 7
3 5 12 13 21
5 6 3
1 5 6 21 30
2 9 3
10 15
11 27182 31415
16 18 33 98 874 989 4848 20458 34365 38117 72030
Sample Output:
173
171
75
3298918744
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length,move,conquer=map(int,input().split())
  arr=list(map(int,input().split()))
  arr.insert(0,0)
  cost=0
  for j in range(length+1):
    if j==0:
      mo=0
      con=0
      for x in range(1,length+1):
        con+=(abs(arr[x]-arr[0]))
      con*=conquer
      cost+=mo
      cost+=con
      out=cost
    else:
      mo=0
      mo=move*abs(arr[j]-arr[j-1])
      cost+=mo
      cost-=((length-j)*conquer*(abs(arr[j]-arr[j-1])))
      out=min(out,cost)
  print(out)
