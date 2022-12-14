# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1622/submission/166874094
'''
Question Link: https://codeforces.com/contest/1622/problem/C

You are given an integer array ๐1,๐2,โฆ,๐๐ and integer ๐.

In one step you can

either choose some index ๐ and decrease ๐๐ by one (make ๐๐=๐๐โ1);
or choose two indices ๐ and ๐ and set ๐๐ equal to ๐๐ (make ๐๐=๐๐).
What is the minimum number of steps you need to make the sum of array โ๐=1๐๐๐โค๐? (You are allowed to make values of array negative).

Input
The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of test cases.

The first line of each test case contains two integers ๐ and ๐ (1โค๐โค2โ105; 1โค๐โค1015) โ the size of array ๐ and upper bound on its sum.

The second line of each test case contains ๐ integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค109) โ the array itself.

It's guaranteed that the sum of ๐ over all test cases doesn't exceed 2โ105.

Output
For each test case, print one integer โ the minimum number of steps to make โ๐=1๐๐๐โค๐.
'''
'''
Sample Input:
4
1 10
20
2 69
6 9
7 8
1 2 1 3 1 2 1
10 1
1 2 3 1 2 6 1 6 8 10
Sample Output:
10
0
2
7
'''
import sys
from math import floor

input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out = 10**10
    length, limit = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    summ = [0]
    for l in range(length):
        summ.append(arr[l] + summ[-1])

    for y in range(length):
        x = arr[0] - floor((limit - summ[length - y] + arr[0]) / (y + 1))
        out = min(out, max(x,0) + y)
    print(out)
