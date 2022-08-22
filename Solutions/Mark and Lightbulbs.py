# Time Limit per Test: 1.5 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1705/submission/164426890
'''
Question Link: https://codeforces.com/contest/1705/problem/D

Mark has just purchased a rack of 𝑛 lightbulbs. The state of the lightbulbs can be described with binary string 𝑠=𝑠1𝑠2…𝑠𝑛, where 𝑠𝑖=𝟷 means that the 𝑖-th lightbulb is turned on, while 𝑠𝑖=𝟶 means that the 𝑖-th lightbulb is turned off.

Unfortunately, the lightbulbs are broken, and the only operation he can perform to change the state of the lightbulbs is the following:

Select an index 𝑖 from 2,3,…,𝑛−1 such that 𝑠𝑖−1≠𝑠𝑖+1.
Toggle 𝑠𝑖. Namely, if 𝑠𝑖 is 𝟶, set 𝑠𝑖 to 𝟷 or vice versa.
Mark wants the state of the lightbulbs to be another binary string 𝑡. Help Mark determine the minimum number of operations to do so.

Input
The first line of the input contains a single integer 𝑞 (1≤𝑞≤104) — the number of test cases.

The first line of each test case contains a single integer 𝑛 (3≤𝑛≤2⋅105) — the number of lightbulbs.

The second line of each test case contains a binary string 𝑠 of length 𝑛 — the initial state of the lightbulbs.

The third line of each test case contains a binary string 𝑡 of length 𝑛 — the final state of the lightbulbs.

It is guaranteed that the sum of 𝑛 across all test cases does not exceed 2⋅105.

Output
For each test case, print a line containing the minimum number of operations Mark needs to perform to transform 𝑠 to 𝑡. If there is no such sequence of operations, print −1.
'''
'''
Sample Input:
4
4
0100
0010
4
1010
0100
5
01001
00011
6
000101
010011
Sample Output:
2
-1
-1
5
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  arr1=input()
  xor1=[]
  pos1=[]
  arr2=input()
  xor2=[]
  pos2=[]
  for l in range(length-1):
    xor1.append(int(arr1[l])^int(arr1[l+1]))
    if (int(arr1[l])^int(arr1[l+1]))==1:
      pos1.append(l)
    xor2.append(int(arr2[l])^int(arr2[l+1]))
    if (int(arr2[l])^int(arr2[l+1]))==1:
      pos2.append(l)
  if arr1[0]!=arr2[0] or arr1[-1]!=arr2[-1] or xor1.count(1)!=xor2.count(1):
    out=-1
  else:
    for p in range(len(pos1)):
      out+=abs(pos1[p]-pos2[p])
  print(out)
