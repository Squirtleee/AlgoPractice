# Time Limit per Test: 2 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1681/submission/161525592
'''
Question Link: https://codeforces.com/contest/1681/problem/D

You are given two integer numbers, 𝑛 and 𝑥. You may perform several operations with the integer 𝑥.

Each operation you perform is the following one: choose any digit 𝑦 that occurs in the decimal representation of 𝑥 at least once, and replace 𝑥 by 𝑥⋅𝑦.

You want to make the length of decimal representation of 𝑥 (without leading zeroes) equal to 𝑛. What is the minimum number of operations required to do that?

Input
The only line of the input contains two integers 𝑛 and 𝑥 (2≤𝑛≤19; 1≤𝑥<10𝑛−1).

Output
Print one integer — the minimum number of operations required to make the length of decimal representation of 𝑥 (without leading zeroes) equal to 𝑛, or −1 if it is impossible.
'''
'''
Sample Input:
2 1
Sample Output:
-1
'''
import sys
input = sys.stdin.readline
#rounds=int(input())
for ii in range(1):
    out=-1
    arr=[]
    length,start=map(int,input().split())
    arr.append([start,0])
    appeared=[]
    
    for num in arr:
        number=str(num[0])
        ope=num[1]
        digit=[d for d in number]
        digit=set(digit)
        for di in digit:
            di=int(di)
            number=int(number)
            if di>1 and number*di not in appeared:
                arr.append([number*di,ope+1])
                appeared.append(number*di)
            if len(str(number*di))>=length:
                out=ope+1
                break
        if out>-1:
            break
    print(out)
