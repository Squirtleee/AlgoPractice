# Time Limit per Test: 1.5 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1712/submission/168390044
'''
Question Link: https://codeforces.com/contest/1712/problem/D

An array of ๐ positive integers ๐1,๐2,โฆ,๐๐ fell down on you from the skies, along with a positive integer ๐โค๐.

You can apply the following operation at most ๐ times:

Choose an index 1โค๐โค๐ and an integer 1โค๐ฅโค109. Then do ๐๐:=๐ฅ (assign ๐ฅ to ๐๐).
Then build a complete undirected weighted graph with ๐ vertices numbered with integers from 1 to ๐, where edge (๐,๐) (1โค๐<๐โค๐) has weight min(๐๐,๐๐+1,โฆ,๐๐).

You have to find the maximum possible diameter of the resulting graph after performing at most ๐ operations.

The diameter of a graph is equal to max1โค๐ข<๐ฃโค๐d(๐ข,๐ฃ), where d(๐ข,๐ฃ) is the length of the shortest path between vertex ๐ข and vertex ๐ฃ.

Input
Each test contains multiple test cases. The first line contains the number of test cases ๐ก (1โค๐กโค104). Description of the test cases follows.

The first line of each test case contains two integers ๐ and ๐ (2โค๐โค105, 1โค๐โค๐).

The second line of each test case contains ๐ positive integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค109).

It is guaranteed that the sum of ๐ over all test cases does not exceed 105.

Output
For each test case print one integer โ the maximum possible diameter of the graph after performing at most ๐ operations.
'''
'''
Sample Input:
6
3 1
2 4 1
3 2
1 9 84
3 1
10 2 6
3 2
179 17 1000000000
2 1
5 9
2 2
4 2
Sample Output:
4
168
10
1000000000
9
1000000000
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length,ope=map(int,input().split())
  arr=list(map(int,input().split()))
  arr2=[]
  arr3=[]
  for l in range(length):
    arr2.append([arr[l],l])
    arr3.append([arr[l],l])
  arr2.sort()
  arr3.sort()
  ans1=-1
  ans2=-1
  
  #strategy 1
  for o in range(ope):
    arr2[o][0]=10**9
  arr2.sort()
  small2=arr2[0][0]
  arr2.sort(key=lambda x: x[1])
  big1=-1
  for t in range(1,length):
    big1=max(min(arr2[t][0],arr2[t-1][0]),big1)
  ans1=min(2*small2,big1)

  #strategy 2
  for o in range(ope-1):
    arr3[o][0]=10**9
  arr3.sort()
  if ope==1:
    small2=arr3[0][0]
    big1=arr3[-1][0]
    if length==1:
      big1=10**9
  else:
    small2=arr3[0][0]
    big1=10**9
  ans2=min(2*small2,big1)
  print(max(ans1,ans2))
