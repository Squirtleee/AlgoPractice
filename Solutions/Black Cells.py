# Time Limit per Test: 4 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1821/submission/203001697
'''
Question Link: https://codeforces.com/contest/1821/problem/D

You are playing with a really long strip consisting of 1018
 white cells, numbered from left to right as 0
, 1
, 2
 and so on. You are controlling a special pointer that is initially in cell 0
. Also, you have a "Shift" button you can press and hold.

In one move, you can do one of three actions:

move the pointer to the right (from cell 𝑥
 to cell 𝑥+1
);
press and hold the "Shift" button;
release the "Shift" button: the moment you release "Shift", all cells that were visited while "Shift" was pressed are colored in black.
(Of course, you can't press Shift if you already hold it. Similarly, you can't release Shift if you haven't pressed it.)
Your goal is to color at least 𝑘
 cells, but there is a restriction: you are given 𝑛
 segments [𝑙𝑖,𝑟𝑖]
 — you can color cells only inside these segments, i. e. you can color the cell 𝑥
 if and only if 𝑙𝑖≤𝑥≤𝑟𝑖
 for some 𝑖
.

What is the minimum number of moves you need to make in order to color at least 𝑘
 cells black?

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains two integers 𝑛
 and 𝑘
 (1≤𝑛≤2⋅105
; 1≤𝑘≤109
) — the number of segments and the desired number of black cells, respectively.

The second line contains 𝑛
 integers 𝑙1,𝑙2,…,𝑙𝑛
 (1≤𝑙1<𝑙2<⋯<𝑙𝑛≤109
), where 𝑙𝑖
 is the left border of the 𝑖
-th segment.

The third line contains 𝑛
 integers 𝑟1,𝑟2,…,𝑟𝑛
 (1≤𝑟𝑖≤109
; 𝑙𝑖≤𝑟𝑖<𝑙𝑖+1−1
), where 𝑟𝑖
 is the right border of the 𝑖
-th segment.

Additional constraints on the input:

every cell belongs to at most one segment;
the sum of 𝑛
 doesn't exceed 2⋅105
.
Output
For each test case, print the minimum number of moves to color at least 𝑘
 cells black, or −1
 if it's impossible.
'''
'''
Sample Input:
4
2 3
1 3
1 4
4 20
10 13 16 19
11 14 17 20
2 3
1 3
1 10
2 4
99 999999999
100 1000000000
Sample Output:
8
-1
7
1000000004
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=10**20
  seg,black=map(int,input().split())
  left=list(map(int,input().split()))
  right=list(map(int,input().split()))
  possible=0
  for s in range(seg):
    possible+=(right[s]-left[s]+1)
  if possible<black:
    print(-1)
    continue
  has=0
  stop_seg=-1
  ones=0
  for s in range(seg):
    has+=(right[s]-left[s]+1)
    ori=has
    if (right[s]==left[s]):
        ones+=1
    if has<black:
      continue
    else:
      cnt=0
      ignore=min(ones,has-black)
      cnt+=(left[s]) # move all the way to the left of the last segment
      cnt+=(2*s-2*ignore) # add the shift and release shift
      cnt+=2
      has-=(right[s]-left[s]+1)
      has-=ignore
      has+=1
      cnt+=(black-has)
      out=min(out,cnt)
      has=ori
  print(out)
      
