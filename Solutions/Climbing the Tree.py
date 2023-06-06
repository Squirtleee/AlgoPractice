# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1810/submission/205439883
'''
Question Link: https://codeforces.com/contest/1810/problem/D

The snails are climbing a tree. The tree height is ℎ
 meters, and snails start at position 0
.

Each snail has two attributes 𝑎
 and 𝑏
 (𝑎>𝑏
). Starting from the 1
-st day, one snail climbs the tree like this: during the daylight hours of the day, he climbs up 𝑎
 meters; during the night, the snail rests, and he slides down 𝑏
 meters. If on the 𝑛
-th day, the snail reaches position ℎ
 for the first time (that is, the top of the tree), he will finish climbing, and we say that the snail spends 𝑛
 days climbing the tree. Note that on the last day of climbing, the snail doesn't necessarily climb up 𝑎
 meters, in case his distance to the top is smaller than 𝑎
.

Unfortunately, you don't know the exact tree height ℎ
 at first, but you know that ℎ
 is a positive integer. There are 𝑞
 events of two kinds.

Event of type 1
: a snail with attributes 𝑎
, 𝑏
 comes and claims that he spent 𝑛
 days climbing the tree. If this message contradicts previously adopted information (i. e. there is no tree for which all previously adopted statements and this one are true), ignore it. Otherwise, adopt it.
Event of type 2
: a snail with attributes 𝑎
, 𝑏
 comes and asks you how many days he will spend if he climbs the tree. You can only give the answer based on the information you have adopted so far. If you cannot determine the answer precisely, report that.
You need to deal with all the events in order.

Input
Each test contains multiple test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. Then follows their description.

The first line of each test case contains one integer 𝑞
 (1≤𝑞≤2⋅105
) — the number of events.

For the following 𝑞
 lines, the first integer of each line is either 1
 or 2
, denoting the event type.

If the event type is 1
, then three integers 𝑎
, 𝑏
, and 𝑛
 (1≤𝑎,𝑏,𝑛≤109
, 𝑎>𝑏
) follow.

If the event type is 2
, then two integers 𝑎
 and 𝑏
 (1≤𝑎,𝑏≤109
, 𝑎>𝑏
) follow.

It is guaranteed that the sum of 𝑞
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output 𝑞
 integers in one line, one for each event, in order. Specifically,

for each event of type 1
, if you adopt the message, output 1
; if you ignore it, output 0
;
for each event of type 2
, output an integer denoting the number of days that the snail will spend. If you cannot determine it, output −1
.
'''
'''
Sample Input:
5
3
1 3 2 5
2 4 1
2 3 2
3
1 6 5 1
2 3 1
2 6 2
3
1 4 2 2
1 2 1 3
2 10 2
9
1 7 3 6
1 2 1 8
2 5 1
1 10 9 7
1 8 1 2
1 10 5 8
1 10 7 7
2 7 4
1 9 4 2
9
1 2 1 6
1 8 5 6
1 4 2 7
2 9 1
1 5 1 4
1 5 2 7
1 7 1 9
1 9 1 4
2 10 8
Sample Output:
1 2 5
1 -1 1
1 0 1
1 0 -1 0 0 0 1 8 0
1 0 0 1 0 0 0 0 1
'''
import sys
from math import ceil
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  events=int(input())
  total=[]
  for e in range(events):
    arr=list(map(int,input().split()))
    total.append(arr)
  low=1
  high=1
  ans=[]
  cnt=0
  for a in total:
    #print(high,low,"hl")
    if len(a)==4:
      cnt+=1
      # data
      a,b,n=a[1],a[2],a[3]
      if n>=2:
        height_min=(a-b)*(n-1)+b+1
        height_max=(a-b)*(n-1)+a
      else:
        height_min=1
        height_max=a
      flag=0
      if cnt==1:
        high=height_max
        low=height_min
        ans.append(1)
      else:
        if height_min<=high and height_max>=low:
          ans.append(1)
          high=min(high,height_max)
          low=max(low,height_min)
        else:
          ans.append(0)
      
    else:
      if cnt==0:
        ans.append(-1)
        continue
      # query
      a,b=a[1],a[2]
      #print(low,high,'lh')
      low_days=-1
      high_days=-1
      low2=low
      low2-=a
      high2=high
      high2-=a
      #print(low2,high2,'lh')
      if low2<=0:
        low_days=1
      else:
        low_days=(low-b-1)//(a-b)+1
      if high2<=0:
        high_days=1
      else:
        high_days=(high-b-1)//(a-b)+1


      if high_days==low_days:
        ans.append(high_days)
      else:
        ans.append(-1)
        
  print(*ans)
        
      
