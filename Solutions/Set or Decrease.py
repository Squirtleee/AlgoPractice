# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1622/submission/166874094
'''
Question Link: https://codeforces.com/contest/1622/problem/C

You are given an integer array 𝑎1,𝑎2,…,𝑎𝑛 and integer 𝑘.

In one step you can

either choose some index 𝑖 and decrease 𝑎𝑖 by one (make 𝑎𝑖=𝑎𝑖−1);
or choose two indices 𝑖 and 𝑗 and set 𝑎𝑖 equal to 𝑎𝑗 (make 𝑎𝑖=𝑎𝑗).
What is the minimum number of steps you need to make the sum of array ∑𝑖=1𝑛𝑎𝑖≤𝑘? (You are allowed to make values of array negative).

Input
The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains two integers 𝑛 and 𝑘 (1≤𝑛≤2⋅105; 1≤𝑘≤1015) — the size of array 𝑎 and upper bound on its sum.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109) — the array itself.

It's guaranteed that the sum of 𝑛 over all test cases doesn't exceed 2⋅105.

Output
For each test case, print one integer — the minimum number of steps to make ∑𝑖=1𝑛𝑎𝑖≤𝑘.
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
