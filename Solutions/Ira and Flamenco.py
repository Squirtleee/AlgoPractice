# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1833/submission/206618259
'''
Question Link: https://codeforces.com/contest/1833/problem/F

Ira loves Spanish flamenco dance very much. She decided to start her own dance studio and found 𝑛
 students, 𝑖
th of whom has level 𝑎𝑖
.

Ira can choose several of her students and set a dance with them. So she can set a huge number of dances, but she is only interested in magnificent dances. The dance is called magnificent if the following is true:

exactly 𝑚
 students participate in the dance;
levels of all dancers are pairwise distinct;
levels of every two dancers have an absolute difference strictly less than 𝑚
.
For example, if 𝑚=3
 and 𝑎=[4,2,2,3,6]
, the following dances are magnificent (students participating in the dance are highlighted in red): [4,2,2,3,6]
, [4,2,2,3,6]
. At the same time dances [4,2,2,3,6]
, [4,2,2,3,6]
, [4,2,2,3,6]
 are not magnificent.

In the dance [4,2,2,3,6]
 only 2
 students participate, although 𝑚=3
.

The dance [4,2,2,3,6]
 involves students with levels 2
 and 2
, although levels of all dancers must be pairwise distinct.

In the dance [4,2,2,3,6]
 students with levels 3
 and 6
 participate, but |3−6|=3
, although 𝑚=3
.

Help Ira count the number of magnificent dances that she can set. Since this number can be very large, count it modulo 109+7
. Two dances are considered different if the sets of students participating in them are different.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — number of testcases.

The first line of each testcase contains integers 𝑛
 and 𝑚
 (1≤𝑚≤𝑛≤2⋅105
) — the number of Ira students and the number of dancers in the magnificent dance.

The second line of each testcase contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — levels of students.

It is guaranteed that the sum of 𝑛
 over all testcases does not exceed 2⋅105
.

Output
For each testcase, print a single integer — the number of magnificent dances. Since this number can be very large, print it modulo 109+7
.
'''
'''
Sample Input:
9
7 4
8 10 10 9 6 11 7
5 3
4 2 2 3 6
8 2
1 5 2 2 3 1 3 3
3 3
3 3 3
5 1
3 4 3 10 7
12 3
5 2 1 1 4 3 5 5 5 2 7 5
1 1
1
3 2
1 2 3
2 2
1 2
Sample Output:
5
2
10
0
5
11
1
2
1
'''
import sys
from collections import Counter
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  mod=10**9+7
  length,m=map(int,input().split())
  arr=list(map(int,input().split()))
  arr.sort()
  cnt=Counter(arr)
  arr2=[arr[0]]
  for l in range(1,length):
    if arr[l]!=arr2[-1]:
      arr2.append(arr[l])
  
  start=0
  end=0
  plus=cnt[arr2[0]]
  for l in range(1,len(arr2)):
    if arr2[l]-arr2[0]>=m or (l+1)>m:
      break
    plus*=cnt[arr2[l]]
    
    end=l
  
  if end-start+1==m:
    out+=plus
    out%=mod
  
  for start in range(1,len(arr2)-m+1):
    plus=plus//cnt[arr2[start-1]]
    while True:
      end+=1
      if end==length:
        end-=1
        break
      if end-start+1==m and arr2[end]-arr2[start]<m:
        plus*=cnt[arr2[end]]
        out+=plus
        out%=mod
        break
      if arr2[end]-arr2[start]>=m:
        end-=1
        break
    #print(plus,start,end,arr2)
      
      
    
  sys.stdout.write(str(out%mod)+'\n')
      
