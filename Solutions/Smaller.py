# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1742/submission/176017397
'''
Question Link: https://codeforces.com/contest/1742/problem/F

Alperen has two strings, π  and π‘ which are both initially equal to "a".

He will perform π operations of two types on the given strings:

1ππ₯ β Append the string π₯ exactly π times at the end of string π . In other words, π :=π +π₯+β―+π₯ξ½ξΎξξξπ times.
2ππ₯ β Append the string π₯ exactly π times at the end of string π‘. In other words, π‘:=π‘+π₯+β―+π₯ξ½ξΎξξξπ times.
After each operation, determine if it is possible to rearrange the characters of π  and π‘ such that π  is lexicographically smallerβ  than π‘.

Note that the strings change after performing each operation and don't go back to their initial states.

β  Simply speaking, the lexicographical order is the order in which words are listed in a dictionary. A formal definition is as follows: string π is lexicographically smaller than string π if there exists a position π such that ππ<ππ, and for all π<π, ππ=ππ. If no such π exists, then π is lexicographically smaller than π if the length of π is less than the length of π. For example, ππππ<πππ and πππ<ππππ, where we write π<π if π is lexicographically smaller than π.

Input
The first line of the input contains an integer π‘ (1β€π‘β€104) β the number of test cases.

The first line of each test case contains an integer π (1β€πβ€105) β the number of operations Alperen will perform.

Then π lines follow, each containing two positive integers π and π (1β€πβ€2; 1β€πβ€105) and a non-empty string π₯ consisting of lowercase English letters β the type of the operation, the number of times we will append string π₯ and the string we need to append respectively.

It is guaranteed that the sum of π over all test cases doesn't exceed 105 and that the sum of lengths of all strings π₯ in the input doesn't exceed 5β105.

Output
For each operation, output "YES", if it is possible to arrange the elements in both strings in such a way that π  is lexicographically smaller than π‘ and "NO" otherwise.
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
