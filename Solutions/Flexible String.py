# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1778/submission/191593394
'''
Question Link: https://codeforces.com/contest/1778/problem/C

You have a string 𝑎
 and a string 𝑏
. Both of the strings have length 𝑛
. There are at most 10
 different characters in the string 𝑎
. You also have a set 𝑄
. Initially, the set 𝑄
 is empty. You can apply the following operation on the string 𝑎
 any number of times:

Choose an index 𝑖
 (1≤𝑖≤𝑛
) and a lowercase English letter 𝑐
. Add 𝑎𝑖
 to the set 𝑄
 and then replace 𝑎𝑖
 with 𝑐
.
For example, Let the string 𝑎
 be "𝚊𝚋𝚎𝚌𝚌𝚊
". We can do the following operations:

In the first operation, if you choose 𝑖=3
 and 𝑐=𝚡
, the character 𝑎3=𝚎
 will be added to the set 𝑄
. So, the set 𝑄
 will be {𝚎}
, and the string 𝑎
 will be "𝚊𝚋𝚡⎯⎯𝚌𝚌𝚊
".
In the second operation, if you choose 𝑖=6
 and 𝑐=𝚜
, the character 𝑎6=𝚊
 will be added to the set 𝑄
. So, the set 𝑄
 will be {𝚎,𝚊}
, and the string 𝑎
 will be "𝚊𝚋𝚡𝚌𝚌𝚜⎯⎯
".
You can apply any number of operations on 𝑎
, but in the end, the set 𝑄
 should contain at most 𝑘
 different characters. Under this constraint, you have to maximize the number of integer pairs (𝑙,𝑟)
 (1≤𝑙≤𝑟≤𝑛
) such that 𝑎[𝑙,𝑟]=𝑏[𝑙,𝑟]
. Here, 𝑠[𝑙,𝑟]
 means the substring of string 𝑠
 starting at index 𝑙
 (inclusively) and ending at index 𝑟
 (inclusively).

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line contains two integers 𝑛
 and 𝑘
 (1≤𝑛≤105
, 0≤𝑘≤10
) — the length of the two strings and the limit on different characters in the set 𝑄
.

The second line contains the string 𝑎
 of length 𝑛
. There is at most 10
 different characters in the string 𝑎
.

The last line contains the string 𝑏
 of length 𝑛
.

Both of the strings 𝑎
 and 𝑏
 contain only lowercase English letters. The sum of 𝑛
 over all test cases doesn't exceed 105
.

Output
For each test case, print a single integer in a line, the maximum number of pairs (𝑙,𝑟)
 satisfying the constraints.
'''
'''
Sample Input
6
3 1
abc
abd
3 0
abc
abd
3 1
xbb
xcd
4 1
abcd
axcb
3 10
abc
abd
10 3
lkwhbahuqa
qoiujoncjb

Sample Output:
6
3
6
6
6
11
'''
import sys
from itertools import combinations
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out=0
    length,lim=map(int,input().split())
    w1=input()
    w2=input()
    diff=set()
    for l in range(length):
        if w1[l]!=w2[l]:
            diff.add(w1[l])
    opt=[]
    for d in diff:
        opt.append(d)
    pos=combinations(opt,min(len(opt),lim))
    ans=0
    cnt=0
    for p in pos:
        temp=0
        change=set(p)
        cnt=0
        for l in range(length):
            if w1[l]!=w2[l] and w1[l] not in change:
                temp+=(((1+cnt))*cnt//2)
                #print(cnt,temp,l)
                cnt=0
            if w1[l]==w2[l] or w1[l] in change:
                cnt+=1
        temp+=(((1+cnt))*cnt//2)
        ans=max(ans,temp)
        #print(cnt,temp)
    print(ans)


