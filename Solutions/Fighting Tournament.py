# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1719/submission/168577582
'''
Question Link: https://codeforces.com/contest/1719/problem/C

Burenka is about to watch the most interesting sporting event of the year — a fighting tournament organized by her friend Tonya.

𝑛 athletes participate in the tournament, numbered from 1 to 𝑛. Burenka determined the strength of the 𝑖-th athlete as an integer 𝑎𝑖, where 1≤𝑎𝑖≤𝑛. All the strength values are different, that is, the array 𝑎 is a permutation of length 𝑛. We know that in a fight, if 𝑎𝑖>𝑎𝑗, then the 𝑖-th participant always wins the 𝑗-th.

The tournament goes like this: initially, all 𝑛 athletes line up in ascending order of their ids, and then there are infinitely many fighting rounds. In each round there is exactly one fight: the first two people in line come out and fight. The winner goes back to the front of the line, and the loser goes to the back.

Burenka decided to ask Tonya 𝑞 questions. In each question, Burenka asks how many victories the 𝑖-th participant gets in the first 𝑘 rounds of the competition for some given numbers 𝑖 and 𝑘. Tonya is not very good at analytics, so he asks you to help him answer all the questions.

Input
The first line contains one integer 𝑡 (1≤𝑡≤104) — the number of test cases. Description of the test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑞 (2≤𝑛≤105, 1≤𝑞≤105) — the number of tournament participants and the number of questions.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛) — the array 𝑎, which is a permutation.

The next 𝑞 lines of a test case contain questions. Each line contains two integers 𝑖 and 𝑘 (1≤𝑖≤𝑛, 1≤𝑘≤109) — the number of the participant and the number of rounds.

It is guaranteed that the sum of 𝑛 and the sum of 𝑞 over all test cases do not exceed 105.

Output
For each Burenka's question, print a single line containing one integer — the answer to the question.
'''
'''
Sample Input:
3
3 1
3 1 2
1 2
4 2
1 3 4 2
4 5
3 2
5 2
1 2 3 5 4
5 1000000000
4 6
Sample Output:
2
0
1
0
4
'''
import sys
from collections import deque
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out=0
    length,ques=map(int,input().split())
    arr=list(map(int,input().split()))
    pos=[0]*length
    data={}
    for e in range(length):
        data[arr[e]]=e

    #start winning pos, wins in the first cycle,value
    biggest=[0,0,0]
    biggest[2]=max(arr)
    biggest[0]=arr.index(biggest[2])
    if biggest[0]==0:
        biggest[1]=length-biggest[0]-1
    else:
        biggest[1]=length-biggest[0]
    #deal w fake big
    large=arr[0]
    ind=0
    cnt=0
    for l in range(1,length):
        if arr[l]<large:
            cnt+=1
        else:
            pos[ind]+=cnt
            large=arr[l]
            ind=l
            cnt=1
    pos[ind]+=cnt


    for q in range(ques):
        place,ro=map(int,input().split())
        place-=1
        if pos[place]==0:
            print(0)
        elif arr[place]<biggest[2]:
            ind=data[arr[place]]
            if ind==0:
                if ro>=ind+pos[place]:
                    print(pos[place])
                else:
                    diff=ind+pos[place]-ro
                    print(max(0,pos[place]-diff))
            else:
                if ro>=ind+pos[place]-1:
                    print(pos[place])
                else:
                    diff=ind+pos[place]-1-ro
                    print(max(0,pos[place]-diff))
        else:
            ind=biggest[0]
            if ro<=length-1:
                if ind==0:
                        diff=ind+pos[place]-ro
                        print(max(0,pos[place]-diff))
                else:
                        diff=ind+pos[place]-1-ro
                        print(max(0,pos[place]-diff))
            else:
                if ind==0:
                    print(ro)
                else:
                    print(ro-(ind-1))
