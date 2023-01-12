# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1768/submission/188232828
'''
Question Link: https://codeforces.com/contest/1768/problem/D

You are given a permutation† 𝑝 of length 𝑛.

In one operation, you can choose two indices 1≤𝑖<𝑗≤𝑛 and swap 𝑝𝑖 with 𝑝𝑗.

Find the minimum number of operations needed to have exactly one inversion‡ in the permutation.

† A permutation is an array consisting of 𝑛 distinct integers from 1 to 𝑛 in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (𝑛=3 but there is 4 in the array).

‡ The number of inversions of a permutation 𝑝 is the number of pairs of indices (𝑖,𝑗) such that 1≤𝑖<𝑗≤𝑛 and 𝑝𝑖>𝑝𝑗.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer 𝑛 (2≤𝑛≤2⋅105).

The second line of each test case contains 𝑛 integers 𝑝1,𝑝2,…,𝑝𝑛 (1≤𝑝𝑖≤𝑛). It is guaranteed that 𝑝 is a permutation.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case output a single integer — the minimum number of operations needed to have exactly one inversion in the permutation. It can be proven that an answer always exists.
'''
'''
Sample Input:
4
2
2 1
2
1 2
4
3 4 1 2
4
2 4 3 1
Sample Output:
0
1
3
1
'''
import sys

input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out = 0
    length = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    cycle = 0
    cycle_id = {}
    id = 1
    for l in range(length):
        ver = l + 1
        per = arr[l]
        if per not in seen:
            seen.add(per)
            cycle_id[per] = id
            cycle += 1
            while per != ver:
                seen.add(per)
                cycle_id[per] = id
                per = arr[per - 1]
            seen.add(per)
            cycle_id[per] = id
            id += 1
    out = length - cycle + 1
    for l in range(length):
        cur = arr[l]
        if cur == length:
            continue
        cur2 = cur + 1
        if cycle_id[cur] == cycle_id[cur2]:
            cycle2 = cycle + 1
        else:
            cycle2 = cycle - 1
        out = min(out, length - cycle2)
    print(out)
