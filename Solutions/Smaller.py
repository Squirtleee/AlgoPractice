# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1742/submission/176017397
'''
Question Link: https://codeforces.com/contest/1742/problem/F

Alperen has two strings, 𝑠 and 𝑡 which are both initially equal to "a".

He will perform 𝑞 operations of two types on the given strings:

1𝑘𝑥 — Append the string 𝑥 exactly 𝑘 times at the end of string 𝑠. In other words, 𝑠:=𝑠+𝑥+⋯+𝑥𝑘 times.
2𝑘𝑥 — Append the string 𝑥 exactly 𝑘 times at the end of string 𝑡. In other words, 𝑡:=𝑡+𝑥+⋯+𝑥𝑘 times.
After each operation, determine if it is possible to rearrange the characters of 𝑠 and 𝑡 such that 𝑠 is lexicographically smaller† than 𝑡.

Note that the strings change after performing each operation and don't go back to their initial states.

† Simply speaking, the lexicographical order is the order in which words are listed in a dictionary. A formal definition is as follows: string 𝑝 is lexicographically smaller than string 𝑞 if there exists a position 𝑖 such that 𝑝𝑖<𝑞𝑖, and for all 𝑗<𝑖, 𝑝𝑗=𝑞𝑗. If no such 𝑖 exists, then 𝑝 is lexicographically smaller than 𝑞 if the length of 𝑝 is less than the length of 𝑞. For example, 𝚊𝚋𝚍𝚌<𝚊𝚋𝚎 and 𝚊𝚋𝚌<𝚊𝚋𝚌𝚍, where we write 𝑝<𝑞 if 𝑝 is lexicographically smaller than 𝑞.

Input
The first line of the input contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains an integer 𝑞 (1≤𝑞≤105) — the number of operations Alperen will perform.

Then 𝑞 lines follow, each containing two positive integers 𝑑 and 𝑘 (1≤𝑑≤2; 1≤𝑘≤105) and a non-empty string 𝑥 consisting of lowercase English letters — the type of the operation, the number of times we will append string 𝑥 and the string we need to append respectively.

It is guaranteed that the sum of 𝑞 over all test cases doesn't exceed 105 and that the sum of lengths of all strings 𝑥 in the input doesn't exceed 5⋅105.

Output
For each operation, output "YES", if it is possible to arrange the elements in both strings in such a way that 𝑠 is lexicographically smaller than 𝑡 and "NO" otherwise.
'''
'''
Sample Input:
3
5
2 1 aa
1 2 a
2 3 a
1 2 b
2 3 abca
2
1 5 mihai
2 2 buiucani
3
1 5 b
2 3 a
2 4 paiu

Sample Output:
YES
NO
YES
NO
YES
NO
YES
NO
NO
YES
'''
import sys
from collections import Counter
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=-1
    ope=int(input())
    cnta=[0]*26
    cntb=[0]*26
    cnta[0]=1
    cntb[0]=1
    for o in range(ope):
        kind,time,word=input().split()
        kind=int(kind)
        time=int(time)
        cnt=Counter(word)
        if kind==1:
            for c in cnt:
                cnta[ord(c)-97]+=(cnt[c]*time)
        else:
            for c in cnt:
                cntb[ord(c)-97]+=(cnt[c]*time)
        otherb=False
        for z in range(1,26):
            if cntb[z]>0:
                otherb=True
                break
        if otherb:
            print('YES')
        elif cnta[0]<cntb[0] and sum(cnta)==cnta[0]:
            print('YES')
        else:
            print('NO')
