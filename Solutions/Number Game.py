# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1749/submission/177170708
'''
Question Link: https://codeforces.com/contest/1749/problem/C

Alice and Bob are playing a game. They have an array of positive integers 𝑎 of size 𝑛.

Before starting the game, Alice chooses an integer 𝑘≥0. The game lasts for 𝑘 stages, the stages are numbered from 1 to 𝑘. During the 𝑖-th stage, Alice must remove an element from the array that is less than or equal to 𝑘−𝑖+1. After that, if the array is not empty, Bob must add 𝑘−𝑖+1 to an arbitrary element of the array. Note that both Alice's move and Bob's move are two parts of the same stage of the game. If Alice can't delete an element during some stage, she loses. If the 𝑘-th stage ends and Alice hasn't lost yet, she wins.

Your task is to determine the maximum value of 𝑘 such that Alice can win if both players play optimally. Bob plays against Alice, so he tries to make her lose the game, if it's possible.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤100) — the number of test cases.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤100) — the size of the array 𝑎.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛).

Output
For each test case, print one integer — the maximum value of 𝑘 such that Alice can win if both players play optimally.
'''
'''
Sample Input:
4
3
1 1 2
4
4 4 4 4
1
1
5
1 3 2 1 1
Sample Output:
2
0
1
3
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=0
    length=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    for k in range(min((length//2)+2,length+1)):
        success=True
        ind=-1
        for l in range(length-1,-1,-1):
            if arr[l]<=k-1+1:
                ind=l
                break
        nope=-1
        for ro in range(1,k+1):
            if ind<=nope:
                success=False
                break
            while arr[ind]>k-ro+1:
                ind-=1
                if ind<=nope:
                    success=False
                    break
            ind-=1
            nope+=1
        if success:
            out=max(out,k)
    print(out)


