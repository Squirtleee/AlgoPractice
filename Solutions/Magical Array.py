# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1704/submission/166497023
'''
Question Link: https://codeforces.com/contest/1704/problem/D

Eric has an array 𝑏 of length 𝑚, then he generates 𝑛 additional arrays 𝑐1,𝑐2,…,𝑐𝑛, each of length 𝑚, from the array 𝑏, by the following way:

Initially, 𝑐𝑖=𝑏 for every 1≤𝑖≤𝑛. Eric secretly chooses an integer 𝑘 (1≤𝑘≤𝑛) and chooses 𝑐𝑘 to be the special array.

There are two operations that Eric can perform on an array 𝑐𝑡:

Operation 1: Choose two integers 𝑖 and 𝑗 (2≤𝑖<𝑗≤𝑚−1), subtract 1 from both 𝑐𝑡[𝑖] and 𝑐𝑡[𝑗], and add 1 to both 𝑐𝑡[𝑖−1] and 𝑐𝑡[𝑗+1]. That operation can only be used on a non-special array, that is when 𝑡≠𝑘.;
Operation 2: Choose two integers 𝑖 and 𝑗 (2≤𝑖<𝑗≤𝑚−2), subtract 1 from both 𝑐𝑡[𝑖] and 𝑐𝑡[𝑗], and add 1 to both 𝑐𝑡[𝑖−1] and 𝑐𝑡[𝑗+2]. That operation can only be used on a special array, that is when 𝑡=𝑘.
Note that Eric can't perform an operation if any element of the array will become less than 0 after that operation.

Now, Eric does the following:

For every non-special array 𝑐𝑖 (𝑖≠𝑘), Eric uses only operation 1 on it at least once.
For the special array 𝑐𝑘, Eric uses only operation 2 on it at least once.
Lastly, Eric discards the array 𝑏.

For given arrays 𝑐1,𝑐2,…,𝑐𝑛, your task is to find out the special array, i.e. the value 𝑘. Also, you need to find the number of times of operation 2 was used on it.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases. Description of test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 (3≤𝑛≤105, 7≤𝑚≤3⋅105) — the number of arrays given to you, and the length of each array.

The next 𝑛 lines contains 𝑚 integers each, 𝑐𝑖,1,𝑐𝑖,2,…,𝑐𝑖,𝑚.

It is guaranteed that each element of the discarded array 𝑏 is in the range [0,106], and therefore 0≤𝑐𝑖,𝑗≤3⋅1011 for all possible pairs of (𝑖,𝑗).

It is guaranteed that the sum of 𝑛⋅𝑚 over all test cases does not exceed 106.

It is guaranteed that the input is generated according to the procedure above.

Output
For each test case, output one line containing two integers — the index of the special array, and the number of times that Operation 2 was performed on it. It can be shown that under the constraints given in the problem, this value is unique and won't exceed 1018, so you can represent it as a 64-bit integer. It can also be shown that the index of the special array is uniquely determined.
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
