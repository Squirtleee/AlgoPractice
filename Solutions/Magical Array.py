# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1704/submission/166497023
'''
Question Link: https://codeforces.com/contest/1704/problem/D

Eric has an array ๐ of length ๐, then he generates ๐ additional arrays ๐1,๐2,โฆ,๐๐, each of length ๐, from the array ๐, by the following way:

Initially, ๐๐=๐ for every 1โค๐โค๐. Eric secretly chooses an integer ๐ (1โค๐โค๐) and chooses ๐๐ to be the special array.

There are two operations that Eric can perform on an array ๐๐ก:

Operation 1: Choose two integers ๐ and ๐ (2โค๐<๐โค๐โ1), subtract 1 from both ๐๐ก[๐] and ๐๐ก[๐], and add 1 to both ๐๐ก[๐โ1] and ๐๐ก[๐+1]. That operation can only be used on a non-special array, that is when ๐กโ ๐.;
Operation 2: Choose two integers ๐ and ๐ (2โค๐<๐โค๐โ2), subtract 1 from both ๐๐ก[๐] and ๐๐ก[๐], and add 1 to both ๐๐ก[๐โ1] and ๐๐ก[๐+2]. That operation can only be used on a special array, that is when ๐ก=๐.
Note that Eric can't perform an operation if any element of the array will become less than 0 after that operation.

Now, Eric does the following:

For every non-special array ๐๐ (๐โ ๐), Eric uses only operation 1 on it at least once.
For the special array ๐๐, Eric uses only operation 2 on it at least once.
Lastly, Eric discards the array ๐.

For given arrays ๐1,๐2,โฆ,๐๐, your task is to find out the special array, i.e. the value ๐. Also, you need to find the number of times of operation 2 was used on it.

Input
The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of test cases. Description of test cases follows.

The first line of each test case contains two integers ๐ and ๐ (3โค๐โค105, 7โค๐โค3โ105) โ the number of arrays given to you, and the length of each array.

The next ๐ lines contains ๐ integers each, ๐๐,1,๐๐,2,โฆ,๐๐,๐.

It is guaranteed that each element of the discarded array ๐ is in the range [0,106], and therefore 0โค๐๐,๐โค3โ1011 for all possible pairs of (๐,๐).

It is guaranteed that the sum of ๐โ๐ over all test cases does not exceed 106.

It is guaranteed that the input is generated according to the procedure above.

Output
For each test case, output one line containing two integers โ the index of the special array, and the number of times that Operation 2 was performed on it. It can be shown that under the constraints given in the problem, this value is unique and won't exceed 1018, so you can represent it as a 64-bit integer. It can also be shown that the index of the special array is uniquely determined.
'''
'''
Sample Input:
2
3 9
0 1 2 0 0 2 1 1 0
0 1 1 1 2 0 0 2 0
0 1 2 0 0 1 2 1 0
3 7
25 15 20 15 25 20 20
26 14 20 14 26 20 20
25 15 20 15 20 20 25
Sample Output:
3 1
3 10
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  numbers,length=map(int,input().split())
  total=set()
  ind1=0
  ind2=0
  to1=0
  to2=0
  for n in range(numbers):
    a=list(map(int,input().split()))
    if to1==0 or to2==0:
      t=0
      for l in range(1,length+1):
        t+=a[l-1]*l
      if to1==0:
        to1=t
        ind1=n+1
      elif t!=to1:
        to2=t
        ind2=n+1
      
  if to1>to2:
    print(ind1,to1-to2)
  else:
    print(ind2,to2-to1)
