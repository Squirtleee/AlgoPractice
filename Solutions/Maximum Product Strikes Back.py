# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1660/submission/162546143
'''
Question Link: https://codeforces.com/contest/1660/problem/D

You are given an array π consisting of π integers. For each π (1β€πβ€π) the following inequality is true: β2β€ππβ€2.

You can remove any number (possibly 0) of elements from the beginning of the array and any number (possibly 0) of elements from the end of the array. You are allowed to delete the whole array.

You need to answer the question: how many elements should be removed from the beginning of the array, and how many elements should be removed from the end of the array, so that the result will be an array whose product (multiplication) of elements is maximal. If there is more than one way to get an array with the maximum product of elements on it, you are allowed to output any of them.

The product of elements of an empty array (array of length 0) should be assumed to be 1.

Input
The first line of input data contains an integer π‘ (1β€π‘β€104) βthe number of test cases in the test.

Then the descriptions of the input test cases follow.

The first line of each test case description contains an integer π (1β€πβ€2β105) βthe length of array π.

The next line contains π integers π1,π2,β¦,ππ (|ππ|β€2) β elements of array π.

It is guaranteed that the sum of π over all test cases does not exceed 2β105.

Output
For each test case, output two non-negative numbers π₯ and π¦ (0β€π₯+π¦β€π) β such that the product (multiplication) of the array numbers, after removing π₯ elements from the beginning and π¦ elements from the end, is maximal.

If there is more than one way to get the maximal product, it is allowed to output any of them. Consider the product of numbers on empty array to be 1.
'''
'''
Sample Input:
5
4
1 2 -1 2
3
1 1 -2
5
2 0 -2 2 -1
3
-2 -1 -1
3
-1 -2 -2
Sample Output:
0 2
3 0
2 0
0 1
1 0
'''
from collections import deque

import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=1
  length=int(input())
  arr=list(map(int,input().split()))
  segment=deque()
  hold=deque()
  start_ind=deque()
  front=length
  back=0
  for l in range(length):
    if arr[l]!=0:
      hold.append(arr[l])
    else:
      if len(hold)>0:
        segment.append(hold)
        start_ind.append(l-len(hold))
        hold=deque()
  if len(hold)>0:
        segment.append(hold)
        start_ind.append(length-len(hold))
  for ss in range(len(segment)):
    s=segment[ss]
    allP=True
    mul=1
    start=-1
    end=-1
    cnt_neg=0
    for numm in range(len(s)):
      num=s[numm]
      if num<0:
        allP=False
        if start==-1:
          start=numm
        end=numm
        cnt_neg+=1
    if allP or cnt_neg%2==0:
      for nu in s:
        mul*=nu
      if mul>out:
        out=mul
        front=start_ind[ss]
        back=length-front-len(s)
    else:
      mul1=1
      mul2=1
      mul3=1
      l1=0
      l2=0
      for z in range(start+1,end):
        mul3*=s[z]
        l1+=1
        l2+=1
      for r in range(end,len(s)):
        mul1*=s[r]
        l1+=1
      for rr in range(start+1):
        mul2*=s[rr]
        l2+=1
      mul1*=mul3
      mul2*=mul3
      if start==end:
        mul1=mul1//s[start]
        mul2=mul2//s[end]
        l1-=1
        l2-=1
      mul=max(mul1,mul2)
      if mul>out:
        out=mul
        if mul1>mul2:
          front=start_ind[ss]+start+1
          back=length-front-l1
        else:
          front=start_ind[ss]
          back=length-front-l2

  print(front,back)
