# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1702/submission/163691293
'''
Quesiton Link: https://codeforces.com/contest/1702/problem/E

Polycarp was recently given a set of ๐ (number ๐ โ even) dominoes. Each domino contains two integers from 1 to ๐.

Can he divide all the dominoes into two sets so that all the numbers on the dominoes of each set are different? Each domino must go into exactly one of the two sets.

For example, if he has 4 dominoes: {1,4}, {1,3}, {3,2} and {4,2}, then Polycarp will be able to divide them into two sets in the required way. The first set can include the first and third dominoes ({1,4} and {3,2}), and the second set โ the second and fourth ones ({1,3} and {4,2}).

Input
The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of test cases.

The descriptions of the test cases follow.

The first line of each test case contains a single even integer ๐ (2โค๐โค2โ105) โ the number of dominoes.

The next ๐ lines contain pairs of numbers ๐๐ and ๐๐ (1โค๐๐,๐๐โค๐) describing the numbers on the ๐-th domino.

It is guaranteed that the sum of ๐ over all test cases does not exceed 2โ105.

Output
For each test case print:

YES, if it is possible to divide ๐ dominoes into two sets so that the numbers on the dominoes of each set are different;
NO if this is not possible.
You can print YES and NO in any case (for example, the strings yEs, yes, Yes and YES will be recognized as a positive answer).
'''
'''
Sample Input:
1
4
1 2
4 3
2 1
3 4
Sample Output:
YES
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out='YES'
  length=int(input())
  s1=set()
  s2=set()
  stack=deque()
  
  for l in range(length):
    p1,p2=map(int,input().split())
    stack.append((p1,p2))

  okay=0
  ori=len(stack)
  while stack:
    ori=len(stack)
    for s in range(len(stack)):
      current=stack.popleft()
      a=current[0]
      b=current[1]
      if a==b:
        out='NO'
        break
      ain1=False
      ain2=False
      bin1=False
      bin2=False
      if a in s1:
        ain1=True
      if a in s2:
        ain2=True
      if b in s1:
        bin1=True
      if b in s2:
        bin2=True
      if ain1 or bin1:
        if bin2 or ain2:
          out='NO'
          break
        else:
          s2.add(a)
          s2.add(b)
      elif ain2 or bin2:
        if bin1 or ain1:
          out='NO'
          break
        else:
          s1.add(a)
          s1.add(b)
      else:
        stack.append((a,b))
    if (ori)==len(stack):
      break
      

  if out=='YES':
    while stack and out=='YES':
      current=stack.popleft()
      a=current[0]
      b=current[1]
      if a==b:
          out='NO'
          break
      ain1=False
      ain2=False
      bin1=False
      bin2=False
      if a in s1:
        ain1=True
      if a in s2:
        ain2=True
      if b in s1:
        bin1=True
      if b in s2:
        bin2=True
      if ain1 or bin1:
        if bin2 or ain2:
          out='NO'
          break
        else:
          s2.add(a)
          s2.add(b)
      elif ain2 or bin2:
        if bin1 or ain1:
          out='NO'
          break
        else:
          s1.add(a)
          s1.add(b)
      else:
        s1.add(a)
        s1.add(b)
      while stack:
        ori=len(stack)
        for s in range(len(stack)):
          current=stack.popleft()
          a=current[0]
          b=current[1]
          if a==b:
            out='NO'
            break
          ain1=False
          ain2=False
          bin1=False
          bin2=False
          if a in s1:
            ain1=True
          if a in s2:
            ain2=True
          if b in s1:
            bin1=True
          if b in s2:
            bin2=True
          if ain1 or bin1:
            if bin2 or ain2:
              out='NO'
              break
            else:
              s2.add(a)
              s2.add(b)
          elif ain2 or bin2:
            if bin1 or ain1:
              out='NO'
              break
            else:
              s1.add(a)
              s1.add(b)
          else:
            stack.append((a,b))
        if (ori)==len(stack):
          break
  print(out)
