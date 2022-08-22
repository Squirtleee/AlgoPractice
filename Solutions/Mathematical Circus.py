# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1719/submission/168550825
'''
Question Link: https://codeforces.com/contest/1719/problem/B

A new entertainment has appeared in Buryatia — a mathematical circus! The magician shows two numbers to the audience — 𝑛 and 𝑘, where 𝑛 is even. Next, he takes all the integers from 1 to 𝑛, and splits them all into pairs (𝑎,𝑏) (each integer must be in exactly one pair) so that for each pair the integer (𝑎+𝑘)⋅𝑏 is divisible by 4 (note that the order of the numbers in the pair matters), or reports that, unfortunately for viewers, such a split is impossible.

Burenka really likes such performances, so she asked her friend Tonya to be a magician, and also gave him the numbers 𝑛 and 𝑘.

Tonya is a wolf, and as you know, wolves do not perform in the circus, even in a mathematical one. Therefore, he asks you to help him. Let him know if a suitable splitting into pairs is possible, and if possible, then tell it.

Input
The first line contains one integer 𝑡 (1≤𝑡≤104) — the number of test cases. The following is a description of the input data sets.

The single line of each test case contains two integers 𝑛 and 𝑘 (2≤𝑛≤2⋅105, 0≤𝑘≤109, 𝑛 is even) — the number of integers and the number being added 𝑘.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, first output the string "YES" if there is a split into pairs, and "NO" if there is none.

If there is a split, then in the following 𝑛2 lines output pairs of the split, in each line print 2 numbers — first the integer 𝑎, then the integer 𝑏.
'''
'''
Sample Input:
4
4 1
2 0
12 10
14 11
Sample Output:
YES
1 2
3 4
NO
YES
3 4
7 8
11 12
2 1
6 5
10 9
YES
1 2
3 4
5 6
7 8
9 10
11 12
13 14
'''
import sys
from collections import deque
from turtle import left
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=0
    n,k=map(int,input().split())
    if k%2==1:
        print('YES')
        for t in range(1,n+1,2):
            print(t,t+1)
    else:
        left=k%4
        need=4-left
        if k%4==0:
            print('NO')
        else:
            group2=deque()
            for y in range(1,n+1):
                if y%4==need:
                    group2.append(y)
            num4=4
            ind=0
            if n%4==0:
                print('YES')
                for q in range(1,n+1):
                    if q%4!=need and q%4>0:
                        if num4<=n:
                            print(q,num4)
                            num4+=4
                        elif ind<len(group2):
                            print(group2[ind],q)
                            ind+=1
            elif n%4!=0 and len(group2)==n//4+1:
                print('YES')
                for q in range(1,n+1):
                    if q%4!=need and q%4>0:
                        if num4<=n:
                            print(q,num4)
                            num4+=4
                        elif ind<len(group2):
                            print(group2[ind],q)
                            ind+=1
            else:
                print('NO')
