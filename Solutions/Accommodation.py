# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1804/submission/197156790
'''
Question Link: https://codeforces.com/contest/1804/problem/D

Annie is an amateur photographer. She likes to take pictures of giant residential buildings at night. She just took a picture of a huge rectangular building that can be seen as a table of 𝑛×𝑚
 windows. That means that the building has 𝑛
 floors and each floor has exactly 𝑚
 windows. Each window is either dark or bright, meaning there is light turned on in the room behind it.

Annies knows that each apartment in this building is either one-bedroom or two-bedroom. Each one-bedroom apartment has exactly one window representing it on the picture, and each two-bedroom apartment has exactly two consecutive windows on the same floor. Moreover, the value of 𝑚
 is guaranteed to be divisible by 4
 and it is known that each floor has exactly 𝑚4
 two-bedroom apartments and exactly 𝑚2
 one-bedroom apartments. The actual layout of apartments is unknown and can be different for each floor.

Annie considers an apartment to be occupied if at least one of its windows is bright. She now wonders, what are the minimum and maximum possible number of occupied apartments if judged by the given picture?

Formally, for each of the floors, she comes up with some particular apartments layout with exactly 𝑚4
 two-bedroom apartments (two consecutive windows) and 𝑚2
 one-bedroom apartments (single window). She then counts the total number of apartments that have at least one bright window. What is the minimum and maximum possible number she can get?

Input
The first line of the input contains two positive integers 𝑛
 and 𝑚
 (1≤𝑛⋅𝑚≤5⋅105
) — the number of floors in the building and the number of windows per floor, respectively. It is guaranteed that 𝑚
 is divisible by 4
.

Then follow 𝑛
 lines containing 𝑚
 characters each. The 𝑗
-th character of the 𝑖
-th line is "0" if the 𝑗
-th window on the 𝑖
-th floor is dark, and is "1" if this window is bright.

Output
Print two integers, the minimum possible number of occupied apartments and the maximum possible number of occupied apartments, assuming each floor can have an individual layout of 𝑚4
 two-bedroom and 𝑚2
 one-bedroom apartments.
'''
'''
Sample Input:
5 4
0100
1100
0110
1010
1011
Sample Output:
7 10
'''

import sys
input = sys.stdin.readline
#rounds = int(input())
for ii in range(1):
  out=0
  floor,window=map(int,input().split())
  house=[]
  for f in range(floor):
    row=input()
    house.append(row)
  small=0
  for h in house:
    seg=[]
    lights=h.count('1')
    cnt=0
    for w in range(window):
      if h[w]=='1':
        cnt+=1
      else:
        seg.append(cnt)
        cnt=0
    seg.append(cnt)
    room=0
    for s in seg:
      room+=s//2
    small+=lights-(min(window//4,room))
  # got small, now deal w big
  big=0
  for h in house:
    seg=[]
    lights=h.count('1')
    cnt=0
    lastone=False
    for w in range(window):
      if h[w]=='1' and not lastone:
        cnt+=1
        lastone=True
      elif h[w]=='1' and lastone:
        seg.append(cnt)
        cnt=1
        lastone=True
      else:
        cnt+=1
        lastone=False
    seg.append(cnt)
    room=0
    #print(seg)
    for s in seg:
      room+=s//2
    big+=lights-(max(0,window//4-room))
  print(small,big)



