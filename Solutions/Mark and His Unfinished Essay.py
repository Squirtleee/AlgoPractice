# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1705/submission/164316723
'''
Question Link: https://codeforces.com/contest/1705/problem/C

One night, Mark realized that there is an essay due tomorrow. He hasn't written anything yet, so Mark decided to randomly copy-paste substrings from the prompt to make the essay.

More formally, the prompt is a string 𝑠 of initial length 𝑛. Mark will perform the copy-pasting operation 𝑐 times. Each operation is described by two integers 𝑙 and 𝑟, which means that Mark will append letters 𝑠𝑙𝑠𝑙+1…𝑠𝑟 to the end of string 𝑠. Note that the length of 𝑠 increases after this operation.

Of course, Mark needs to be able to see what has been written. After copying, Mark will ask 𝑞 queries: given an integer 𝑘, determine the 𝑘-th letter of the final string 𝑠.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

The first line of each test case contains three integers 𝑛, 𝑐, and 𝑞 (1≤𝑛≤2⋅105, 1≤𝑐≤40, and 1≤𝑞≤104) — the length of the initial string 𝑠, the number of copy-pasting operations, and the number of queries, respectively.

The second line of each test case contains a single string 𝑠 of length 𝑛. It is guaranteed that 𝑠 only contains lowercase English letters.

The following 𝑐 lines describe the copy-pasting operation. Each line contains two integers 𝑙 and 𝑟 (1≤𝑙≤𝑟≤1018). It is also guaranteed that 𝑟 does not exceed the current length of 𝑠.

The last 𝑞 lines of each test case describe the queries. Each line contains a single integer 𝑘 (1≤𝑘≤1018). It is also guaranteed that 𝑘 does not exceed the final length of 𝑠.

It is guaranteed that the sum of 𝑛 and 𝑞 across all test cases does not exceed 2⋅105 and 104, respectively.

Output
For each query, print the 𝑘-th letter of the final string 𝑠.
'''
'''
Sample Input:
2
4 3 3
mark
1 4
5 7
3 8
1
10
12
7 3 3
creamii
2 3
3 4
2 9
9
11
12
Sample Output:
m
a
r
e
a
r
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length,ope,query=map(int,input().split())
  prompt=input()
  fragment=deque()
  fragment.append((0,length-1,length-1))
  for o in range(ope):
    start,end=map(int,input().split())
    start-=1
    end-=1
    fragment.append((start,end,fragment[-1][2]+end-start+1))

  f_len=len(fragment)
  for q in range(query):
    ask=int(input())
    ask-=1
    cur=f_len-1
    while cur!=0:
      l=0
      r=cur
      while r>l:
        ind=(l+r)//2
        if fragment[ind][2]<ask:
          l=ind+1
        else:
          r=ind
      cur=l
      last=fragment[cur][1]
      first=fragment[cur][0]
      ask=last-(fragment[cur][2]-ask)
    print(prompt[ask])
