# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1775/submission/189010130
'''
Question Link: https://codeforces.com/contest/1775/problem/C

Petya and his friend, robot Petya++, like to solve exciting math problems.

One day Petya++ came up with the numbers 𝑛 and 𝑥 and wrote the following equality on the board:
𝑛 & (𝑛+1) & … & 𝑚=𝑥,
where & denotes the bitwise AND operation. Then he suggested his friend Petya find such a minimal 𝑚 (𝑚≥𝑛) that the equality on the board holds.

Unfortunately, Petya couldn't solve this problem in his head and decided to ask for computer help. He quickly wrote a program and found the answer.

Can you solve this difficult problem?
'''
'''
Sample Input:
5
10 8
10 10
10 42
20 16
1000000000000000000 0
Sample Output:
12
10
-1
24
1152921504606846976
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  start,goal=map(int,input().split())
  if goal==start:
    print(start)
  elif goal>start:
    print(-1)
  else:
    num1=bin(start)[2:]
    num2=bin(goal)[2:]
    if len(num1)>len(num2):
      num2='0'*(len(num1)-len(num2))+num2 
    
    first=False
    diff=-1
    same=-1
    for l in range(len(num1)):
      if num1[l]=='1' and num2[l]=='0':
        if first==False:
          first=True
          diff=l
          break
      if num1[l]=='1' and num2[l]=='1':
        same=l
    
    nope=False
    for d in range(diff,len(num2)):
      if num2[d]=='1':
        print(-1)
        nope=True
        break
    if not nope and diff==0:
      print(2**len(num1))
      continue
    if not nope and same==diff-1 and same>-1:
      print(-1)
      nope=True
      continue
    if not nope:
      out=0
      for y in range(diff):
        if num1[y]=='1':
          out+=(2**(len(num1)-y-1))
      out+=(2**(len(num1)-diff))
      print(out)
