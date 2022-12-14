# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1705/submission/164316723
'''
Question Link: https://codeforces.com/contest/1705/problem/C

One night, Mark realized that there is an essay due tomorrow. He hasn't written anything yet, so Mark decided to randomly copy-paste substrings from the prompt to make the essay.

More formally, the prompt is a string ๐  of initial length ๐. Mark will perform the copy-pasting operation ๐ times. Each operation is described by two integers ๐ and ๐, which means that Mark will append letters ๐ ๐๐ ๐+1โฆ๐ ๐ to the end of string ๐ . Note that the length of ๐  increases after this operation.

Of course, Mark needs to be able to see what has been written. After copying, Mark will ask ๐ queries: given an integer ๐, determine the ๐-th letter of the final string ๐ .

Input
The first line contains a single integer ๐ก (1โค๐กโค1000) โ the number of test cases.

The first line of each test case contains three integers ๐, ๐, and ๐ (1โค๐โค2โ105, 1โค๐โค40, and 1โค๐โค104) โ the length of the initial string ๐ , the number of copy-pasting operations, and the number of queries, respectively.

The second line of each test case contains a single string ๐  of length ๐. It is guaranteed that ๐  only contains lowercase English letters.

The following ๐ lines describe the copy-pasting operation. Each line contains two integers ๐ and ๐ (1โค๐โค๐โค1018). It is also guaranteed that ๐ does not exceed the current length of ๐ .

The last ๐ lines of each test case describe the queries. Each line contains a single integer ๐ (1โค๐โค1018). It is also guaranteed that ๐ does not exceed the final length of ๐ .

It is guaranteed that the sum of ๐ and ๐ across all test cases does not exceed 2โ105 and 104, respectively.

Output
For each query, print the ๐-th letter of the final string ๐ .
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
