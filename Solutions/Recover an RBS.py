# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1709/submission/165202951
'''
Question Link: https://codeforces.com/contest/1709/problem/C

A bracket sequence is a string containing only characters "(" and ")". A regular bracket sequence (or, shortly, an RBS) is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "1" and "+" between the original characters of the sequence. For example:

bracket sequences "()()" and "(())" are regular (the resulting expressions are: "(1)+(1)" and "((1+1)+1)");
bracket sequences ")(", "(" and ")" are not.
There was an RBS. Some brackets have been replaced with question marks. Is it true that there is a unique way to replace question marks with brackets, so that the resulting sequence is an RBS?

Input
The first line contains a single integer 𝑡 (1≤𝑡≤5⋅104) — the number of testcases.

The only line of each testcase contains an RBS with some brackets replaced with question marks. Each character is either '(', ')' or '?'. At least one RBS can be recovered from the given sequence.

The total length of the sequences over all testcases doesn't exceed 2⋅105.

Output
For each testcase, print "YES" if the way to replace question marks with brackets, so that the resulting sequence is an RBS, is unique. If there is more than one way, then print "NO".
'''
'''
Sample Input:
5
(?))
??????
()
??
?(?)()?)
Sample Output:
YES
NO
YES
YES
NO
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out='NO'
  can=[0]
  seq=input()
  seq=[s for s in seq]
  seq.pop(-1)
  left=seq.count('(')
  right=seq.count(')')
  length=len(seq)
  question=length-left-right
  needl=length//2-left
  needr=length//2-right
  if needl>0 and needr>0:
    out='NO'
  else:
    out='YES'
  ri=False
  for s in range(length):
    if seq[s]=='?':
      if needl>1:
        seq[s]='('
        needl-=1
      elif needl==1 and needr>0 and ri==False:
        seq[s]=')'
        needr-=1
        ri=True
      elif needl==1 and ri:
        seq[s]='('
        needl-=1
      else:
        seq[s]=')'
  cntl=0
  cntr=0
  for l in range(length):
    if seq[l]=='(':
      cntl+=1
    else:
      cntr+=1
    if cntl<cntr:
      out='YES'
      break
  print(out)
