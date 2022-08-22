# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1615/submission/165886283	
'''
Question Link: https://codeforces.com/contest/1615/problem/C

There are 𝑛 candles on a Hanukkah menorah, and some of its candles are initially lit. We can describe which candles are lit with a binary string 𝑠, where the 𝑖-th candle is lit if and only if 𝑠𝑖=1.


Initially, the candle lights are described by a string 𝑎. In an operation, you select a candle that is currently lit. By doing so, the candle you selected will remain lit, and every other candle will change (if it was lit, it will become unlit and if it was unlit, it will become lit).

You would like to make the candles look the same as string 𝑏. Your task is to determine if it is possible, and if it is, find the minimum number of operations required.

Input
The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases. Then 𝑡 cases follow.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤105) — the number of candles.

The second line contains a string 𝑎 of length 𝑛 consisting of symbols 0 and 1 — the initial pattern of lights.

The third line contains a string 𝑏 of length 𝑛 consisting of symbols 0 and 1 — the desired pattern of lights.

It is guaranteed that the sum of 𝑛 does not exceed 105.

Output
For each test case, output the minimum number of operations required to transform 𝑎 to 𝑏, or −1 if it's impossible.
'''
'''
Sample Input:
5
5
11010
11010
2
01
11
3
000
101
9
100010111
101101100
9
001011011
011010101
Sample Output:
0
1
-1
3
4
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=10**20
    length=int(input())
    str1=input()
    str2=input()
    if str1.count('1')!=str2.count('1') and str1.count('0')+1!=str2.count('1'):
        out=-1
    elif str1.count('1')==str2.count('1'):
        # if even is possible
        cnt2=0
        for l in range(length):
            if str1[l]!=str2[l]:
                cnt2+=1
        out=cnt2

        # if odd is possible
    cnt1_1=1
    cnt1_2=1
    str1=[s for s in str1]
    str1.pop(-1)
    str2=[f for f in str2]
    str2.pop(-1)
    ind1=-1
    ind2=-1
    if str1.count('0')+1==str2.count('1'):
        for l in range(length):
            if str1[l]=='1' and str2[l]=='0' and ind1==-1:
                ind1=l
            elif str1[l]=='1' and str2[l]=='1' and ind2==-1:
                ind2=l
            if str1[l]=='1':
                str1[l]='0'
            else:
                str1[l]='1'
        if ind1>-1:
            str1[ind1]='1'
            for l in range(length):
                if str1[l]!=str2[l]:
                    cnt1_2+=1
            str1[ind1]='0'
            out=min(out,cnt1_2)
        if ind2>-1:
            str1[ind2]='1'
            for l in range(length):
                if str1[l]!=str2[l]:
                    cnt1_1+=1
            str1[ind2]='0'
            out=min(out,cnt1_1)
    print(out)
