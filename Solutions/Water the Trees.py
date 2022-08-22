# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1661/submission/163185349
'''
Question Link: https://codeforces.com/contest/1661/problem/C

There are 𝑛 trees in a park, numbered from 1 to 𝑛. The initial height of the 𝑖-th tree is ℎ𝑖.

You want to water these trees, so they all grow to the same height.

The watering process goes as follows. You start watering trees at day 1. During the 𝑗-th day you can:

Choose a tree and water it. If the day is odd (e.g. 1,3,5,7,…), then the height of the tree increases by 1. If the day is even (e.g. 2,4,6,8,…), then the height of the tree increases by 2.
Or skip a day without watering any tree.
Note that you can't water more than one tree in a day.

Your task is to determine the minimum number of days required to water the trees so they grow to the same height.

You have to answer 𝑡 independent test cases.

Input
The first line of the input contains one integer 𝑡 (1≤𝑡≤2⋅104) — the number of test cases.

The first line of the test case contains one integer 𝑛 (1≤𝑛≤3⋅105) — the number of trees.

The second line of the test case contains 𝑛 integers ℎ1,ℎ2,…,ℎ𝑛 (1≤ℎ𝑖≤109), where ℎ𝑖 is the height of the 𝑖-th tree.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 3⋅105 (∑𝑛≤3⋅105).

Output
For each test case, print one integer — the minimum number of days required to water the trees, so they grow to the same height.
'''
'''
Sample Input:
3
3
1 2 4
5
4 4 3 5 5
7
2 5 4 8 3 7 4
Sample Output:
4
3
16
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  arr=list(map(int,input().split()))
  days=0
  big=max(arr)
  left=[]
  odd=0
  even=0
  for l in range(length):
    left.append((big-arr[l]))
    if (big-arr[l])%2==1:
      odd+=1
    even+=((big-arr[l])//2)


  if odd>even:
    days+=(odd*2-1)
  elif odd==even:
    days+=(odd+even)
  else:
    days+=(odd*2)
    even-=odd
    odd=0
    days+=4*(2*even//6)
    even=(2*even)%6
    if even==2:
      days+=2
    elif even==4:
      days+=3

  days2=days
  days=0
  big=big+1
  left=[]
  odd=0
  even=0
  for l in range(length):
    left.append((big-arr[l]))
    if (big-arr[l])%2==1:
      odd+=1
    even+=((big-arr[l])//2)

  if odd>even:
    days+=(odd*2-1)
  elif odd==even:
    days+=(odd+even)
  else:
    days+=(odd*2)
    even-=odd
    odd=0
    days+=4*(2*even//6)
    even=(2*even)%6
    if even==2:
      days+=2
    elif even==4:
      days+=3

  print(min(days,days2))
