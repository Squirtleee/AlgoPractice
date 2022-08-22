# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1720/submission/168139417
'''
Question Link: https://codeforces.com/contest/1712/problem/C

You are given an array of 𝑛 positive integers 𝑎1,𝑎2,…,𝑎𝑛.

In one operation you do the following:

Choose any integer 𝑥.
For all 𝑖 such that 𝑎𝑖=𝑥, do 𝑎𝑖:=0 (assign 0 to 𝑎𝑖).
Find the minimum number of operations required to sort the array in non-decreasing order.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤104). Description of the test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤105).

The second line of each test case contains 𝑛 positive integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛).

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
For each test case print one integer — the minimum number of operations required to sort the array in non-decreasing order.
'''
'''
Sample Input:
5
3
3 3 2
4
1 3 1 3
5
4 1 5 3 2
4
2 4 1 2
1
1
Sample Output:
1
2
4
3
0
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=0
    length=int(input())
    arr=list(map(int,input().split()))
    change=set()
    potential=set()
    potential.add(arr[0])
    for l in range(1,length):
        if arr[l] in change:
            arr[l]=0
        if arr[l]<arr[l-1]:
            for p in potential:
                change.add(p)
            potential=set()
            out=len(change)
            if arr[l] in change:
                arr[l]=0
        if arr[l]!=0:
            potential.add(arr[l])
    print(out)
