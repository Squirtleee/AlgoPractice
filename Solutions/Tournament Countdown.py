# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1720/submission/167346830
'''
Question Link: https://codeforces.com/contest/1713/problem/D

This is an interactive problem.

There was a tournament consisting of 2𝑛 contestants. The 1-st contestant competed with the 2-nd, the 3-rd competed with the 4-th, and so on. After that, the winner of the first match competed with the winner of second match, etc. The tournament ended when there was only one contestant left, who was declared the winner of the tournament. Such a tournament scheme is known as the single-elimination tournament.

You don't know the results, but you want to find the winner of the tournament. In one query, you select two integers 𝑎 and 𝑏, which are the indices of two contestants. The jury will return 1 if 𝑎 won more matches than 𝑏, 2 if 𝑏 won more matches than 𝑎, or 0 if their number of wins was equal.

Find the winner in no more than ⌈1/3⋅2^(n+1)⌉ queries. Here ⌈𝑥⌉ denotes the value of 𝑥 rounded up to the nearest integer.

Note that the tournament is long over, meaning that the results are fixed and do not depend on your queries.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤214) — the number of test cases.

The only line of input contains a single integer 𝑛 (1≤𝑛≤17).

It is guaranteed that the sum of 2𝑛 over all test cases does not exceed 217.

Interaction
The interaction for each test case begins by reading the integer 𝑛.

To make a query, output "? a b" (1≤𝑎,𝑏≤2𝑛) without quotes. Afterwards, you should read one single integer — the answer for your query. You can make at most ⌈13⋅2𝑛+1⌉ such queries in each test case.

If you receive the integer −1 instead of an answer or a valid value of 𝑛, it means your program has made an invalid query, has exceed the limit of queries, or has given incorrect answer on the previous test case. Your program must terminate immediately to receive a Wrong Answer verdict. Otherwise you can get an arbitrary verdict because your solution will continue to read from a closed stream.

When you are ready to give the final answer, output "! x" (1≤𝑥≤2𝑛) without quotes — the winner of the tournament. Giving this answer does not count towards the limit of queries. After solving a test case, your program should move to the next one immediately. After solving all test cases, your program should be terminated immediately.
'''
'''
Sample Input:
1
3

2

0

2

Sample Output:


? 1 4

? 1 6

? 5 7

! 7
'''
import sys,os

p, q = "?".encode(), "!".encode()
def ask(a,b):
  os.write(1, b"%s %d %d\n" % (p, a, b))

from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=0
    power=int(input())
  
    if power==1:
      ask(1,2)
      res=int(input())
      if res==1:
        print('!',str(1),flush=True)
      else:
        print('!',str(2),flush=True)
      continue
      
    ppl=2**power
    win=deque()
    long=ppl
    while long>1:
        if len(win)==0:
            for l in range(1,ppl+1,4):
                ask(l,l+3)
                res=int(input())
                if res==0:
                    ask(l+1,l+2)
                    res=int(input())
                    if res==1:
                      win.append(l+1)
                    else:
                      win.append(l+2)
                elif res==1:
                    ask(l,l+2)
                    res=int(input())
                    if res==1:
                      win.append(l)
                    else:
                      win.append(l+2)
                elif res==2:
                    ask(l+1,l+3)
                    res=int(input())
                    if res==1:
                      win.append(l+1)
                    else:
                      win.append(l+3)
        elif long==2:
          ask(win[0],win[1])
          hold=deque()
          res=int(input())
          if res==1:
            hold.append(win[0])
          else:
            hold.append(win[1])
          win=hold
        else:
            hold=deque()
            for w in range(0,long,4):
                ask(win[w],win[w+3])
                res=int(input())
                if res==0:
                    ask(win[w+1],win[w+2])
                    res=int(input())
                    if res==1:
                      hold.append(win[w+1])
                    else:
                      hold.append(win[w+2])
                elif res==1:
                    ask(win[w],win[w+2])
                    res=int(input())
                    if res==1:
                      hold.append(win[w])
                    else:
                      hold.append(win[w+2])
                elif res==2:
                    ask(win[w+1],win[w+3])
                    res=int(input())
                    if res==1:
                      hold.append(win[w+1])
                    else:
                      hold.append(win[w+3])
            win=hold
        long=long//4
    print('!',win[0],flush=True)
