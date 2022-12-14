# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1706/submission/164838668
'''
Question Link: https://codeforces.com/contest/1706/problem/C

Qpwoeirut has taken up architecture and ambitiously decided to remodel his city.

Qpwoeirut's city can be described as a row of ๐ buildings, the ๐-th (1โค๐โค๐) of which is โ๐ floors high. You can assume that the height of every floor in this problem is equal. Therefore, building ๐ is taller than the building ๐ if and only if the number of floors โ๐ in building ๐ is larger than the number of floors โ๐ in building ๐.

Building ๐ is cool if it is taller than both building ๐โ1 and building ๐+1 (and both of them exist). Note that neither the 1-st nor the ๐-th building can be cool.

To remodel the city, Qpwoeirut needs to maximize the number of cool buildings. To do this, Qpwoeirut can build additional floors on top of any of the buildings to make them taller. Note that he cannot remove already existing floors.

Since building new floors is expensive, Qpwoeirut wants to minimize the number of floors he builds. Find the minimum number of floors Qpwoeirut needs to build in order to maximize the number of cool buildings.

Input
The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of test cases.

The first line of each test case contains the single integer ๐ (3โค๐โค105) โ the number of buildings in Qpwoeirut's city.

The second line of each test case contains ๐ integers โ1,โ2,โฆ,โ๐ (1โคโ๐โค109) โ the number of floors in each of the buildings of the city.

It is guaranteed that the sum of ๐ over all test cases does not exceed 2โ105.

Output
For each test case, print a single integer โ the minimum number of additional floors Qpwoeirut needs to build in order to maximize the number of cool buildings.
'''
'''
Sample Input:
6
3
2 1 2
5
1 2 1 4 3
6
3 1 4 5 5 2
8
4 2 1 3 5 3 6 1
6
1 10 1 1 10 1
8
1 10 11 1 10 11 10 1
Sample Output:
2
0
3
3
0
4
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  arr=list(map(int,input().split()))
  cool=[0]
  for l in range(1,length-1):
    if arr[l]>arr[l-1] and arr[l]>arr[l+1]:
      cool.append(0)
    else:
      cool.append(max(arr[l+1],arr[l-1])-arr[l]+1)
  cool.append(0)
  if length%2==1:
    for c in range(1,length,2):
      out+=cool[c]
  else:
    total=0
    space=1
    first=0
    for c in range(2,length-1,2):
      first+=cool[c]
    total=first
    while space<length-2:
      first+=cool[space]
      first-=cool[space+1]
      space+=2
      total=min(total,first)
    out=total
  print(out)
