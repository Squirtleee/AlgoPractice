# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1777/submission/190152830
'''
Quesiton Link: https://codeforces.com/contest/1777/problem/C

A school has to decide on its team for an international quiz. There are 𝑛
 students in the school. We can describe the students using an array 𝑎
 where 𝑎𝑖
 is the smartness of the 𝑖
-th (1≤𝑖≤𝑛
) student.

There are 𝑚
 topics 1,2,3,…,𝑚
 from which the quiz questions will be formed. The 𝑖
-th student is considered proficient in a topic 𝑇
 if (𝑎𝑖mod𝑇)=0
. Otherwise, he is a rookie in that topic.

We say that a team of students is collectively proficient in all the topics if for every topic there is a member of the team proficient in this topic.

Find a team that is collectively proficient in all the topics such that the maximum difference between the smartness of any two students in that team is minimized. Output this difference.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line of each test case contains 𝑛
 and 𝑚
 (1≤𝑛,𝑚≤105
).

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤105
).

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105
.

It is guaranteed that the sum of 𝑚
 over all test cases does not exceed 105
.

Output
For each test case, print the answer on a new line. If there is no solution, output −1.
'''
'''
Sample Input:
3
2 4
3 7
4 2
3 7 2 9
5 7
6 4 3 5 7
Sample Output:
-1
0
3
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length,smart=map(int,input().split())
  stu=list(map(int,input().split()))
  stu.sort()
  has=set()
  
  left=0
  factors_ind={}
  smart_stu=[0]*(smart+1)

  has=set()
  
  for l in range(length):
    factors_ind[l]=set()
    for f in range(1,int(stu[l]**0.5)+1):
      if stu[l]%f==0:
        if f<=smart:
          has.add(f)
        if stu[l]//f<=smart:
          has.add(stu[l]//f)

  nope=False
  for w in range(1,smart+1):
    if w not in has:
      nope=True
      break
  if nope:
    print(-1)
  else:
    left=0
    right=0
    cnt=0
    unique=set()
    for f in range(1,int(stu[0]**0.5)+1):
      if stu[0]%f==0:
        if f<=smart:
          smart_stu[f]+=1
          unique.add(f)
        if stu[0]//f<=smart:
          smart_stu[stu[0]//f]+=1
          unique.add(stu[0]//f)
    if len(unique)>=smart:
      print(0)
    else:
      diff=10**20
      for r in range(1,length):
        #print(stu[r],left,r,stu)
        for f in range(1,int(stu[r]**0.5)+1):
          if stu[r]%f==0:
            if f<=smart:
              smart_stu[f]+=1
              unique.add(f)
            if stu[r]//f<=smart:
              smart_stu[stu[r]//f]+=1
              unique.add(stu[r]//f)
          #print(unique,f,stu[r]//f,stu[r])
          
        while len(unique)>=smart:
          diff2=stu[r]-stu[left]
          diff=min(diff,diff2)
          for f in range(1,int(stu[left]**0.5)+1):
            if stu[left]%f==0:
              if f<=smart:
                smart_stu[f]-=1
                if smart_stu[f]==0:
                  unique.remove(f)
              if stu[left]//f<=smart:
                smart_stu[stu[left]//f]-=1
                if smart_stu[stu[left]//f]==0:
                  unique.remove(stu[left]//f)
          left+=1
          
          
      print(diff)
