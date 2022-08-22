# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1669/submission/163178260
'''
Question Link: https://codeforces.com/contest/1669/problem/G

There is a grid with 𝑛 rows and 𝑚 columns, and three types of cells:

An empty cell, denoted with '.'.
A stone, denoted with '*'.
An obstacle, denoted with the lowercase Latin letter 'o'.
All stones fall down until they meet the floor (the bottom row), an obstacle, or other stone which is already immovable. (In other words, all the stones just fall down as long as they can fall.)

Simulate the process. What does the resulting grid look like?

Input
The input consists of multiple test cases. The first line contains an integer 𝑡 (1≤𝑡≤100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 (1≤𝑛,𝑚≤50) — the number of rows and the number of columns in the grid, respectively.

Then 𝑛 lines follow, each containing 𝑚 characters. Each of these characters is either '.', '*', or 'o' — an empty cell, a stone, or an obstacle, respectively.

Output
For each test case, output a grid with 𝑛 rows and 𝑚 columns, showing the result of the process.

You don't need to output a new line after each test, it is in the samples just for clarity.
'''
'''
Sample Input:
3
6 10
.*.*....*.
.*.......*
...o....o.
.*.*....*.
..........
.o......o*
2 9
...***ooo
.*o.*o.*o
5 5
*****
*....
*****
....*
*****
Sample Output:
..........
...*....*.
.*.o....o.
.*........
.*......**
.o.*....o*

....**ooo
.*o**o.*o

.....
*...*
*****
*****
*****
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  rows,cols=map(int,input().split())
  mapp=[]
  for ro in range(rows):
    r=input()
    r=[p for p in r]
    r.pop(-1)
    mapp.append(r)
  out=[]
  for rr in range(rows):
    hold=[]
    for co in range(cols):
      hold.append('.')
    out.append(hold)
  col_stone=[rows-1]*cols
  for rr in range(rows-1,-1,-1):
    for cc in range(cols):
      if mapp[rr][cc]=='o':
        col_stone[cc]=(rr-1)
        out[rr][cc]='o'
      elif mapp[rr][cc]=='*':
        out[col_stone[cc]][cc]='*'
        col_stone[cc]-=1
  for o in out:
    print(''.join(o))
