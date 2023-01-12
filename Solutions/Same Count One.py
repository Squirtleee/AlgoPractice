# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1774/submission/186530579
'''
Question Link: https://codeforces.com/contest/1774/problem/D

ChthollyNotaSeniorious received a special gift from AquaMoon: 𝑛 binary arrays of length 𝑚. AquaMoon tells him that in one operation, he can choose any two arrays and any position 𝑝𝑜𝑠 from 1 to 𝑚, and swap the elements at positions 𝑝𝑜𝑠 in these arrays.

He is fascinated with this game, and he wants to find the minimum number of operations needed to make the numbers of 1s in all arrays the same. He has invited you to participate in this interesting game, so please try to find it!

If it is possible, please output specific exchange steps in the format described in the output section. Otherwise, please output −1.

Input
The first line of the input contains a single integer 𝑡 (1≤𝑡≤2⋅104)  — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 (2≤𝑛≤105, 2≤𝑚≤105).

The 𝑖-th of the following 𝑛 lines contains 𝑚 integers 𝑎𝑖,1,𝑎𝑖,2,…,𝑎𝑖,𝑚 (0≤𝑎𝑖,𝑗≤1)  — the elements of the 𝑖-th array.

It is guaranteed that the sum of 𝑛⋅𝑚 over all test cases does not exceed 106.

Output
For each test case, if the objective is not achievable, output −1.

Otherwise, in the first line output 𝑘 (0≤𝑘≤𝑚𝑛)  — the minimum number of operations required.

The 𝑖-th of the following 𝑘 lines should contain 3 integers, 𝑥𝑖,𝑦𝑖,𝑧𝑖 (1≤𝑥𝑖,𝑦𝑖≤𝑛,1≤𝑧𝑖≤𝑚), which describe an operation that swap 𝑎𝑥𝑖,𝑧𝑖,𝑎𝑦𝑖,𝑧𝑖: swap the 𝑧𝑖-th number of the 𝑥𝑖-th and 𝑦𝑖-th arrays.
'''
'''
Sample Input:
3
3 4
1 1 1 0
0 0 1 0
1 0 0 1
4 3
1 0 0
0 1 1
0 0 1
0 0 0
2 2
0 0
0 1
Sample Output:
1
2 1 1
1
4 2 2
-1
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  roww,length=map(int,input().split())
  arr=[]
  sum1=0
  ans=[]
  for r in range(roww):
    ar=list(map(int,input().split()))
    arr.append(ar)
    sum1+=ar.count(1)
  if sum1%roww>0:
    out=-1
    print(out)
  else:
    avg=sum1//roww
    less={}
    less2=set()
    more={}
    more2=set()
    for r in range(roww):
      row=arr[r]
      c1=row.count(1)
      if c1<avg:
        less[r]=c1
        less2.add(r)
      elif c1>avg:
        more[r]=c1
        more2.add(r)
    for c in range(length):
      need=[]
      extra=[]
      for r in range(roww):
        if arr[r][c]==0 and r in less:
          need.append(r)
        if arr[r][c]==1 and r in more:
          extra.append(r)
      ll=min(len(need),len(extra))
      for l in range(ll):
        ans.append((extra[l]+1,need[l]+1,c+1))
        less[need[l]]+=1
        if less[need[l]]==avg:
          less.pop(need[l])
        more[extra[l]]-=1
        if more[extra[l]]==avg:
          more.pop(extra[l])
    print(len(ans))
    for a in ans:
      print(a[0],a[1],a[2])
