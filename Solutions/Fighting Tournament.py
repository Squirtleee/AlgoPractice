# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1719/submission/168577582
'''
Question Link: https://codeforces.com/contest/1719/problem/C

Burenka is about to watch the most interesting sporting event of the year โ a fighting tournament organized by her friend Tonya.

๐ athletes participate in the tournament, numbered from 1 to ๐. Burenka determined the strength of the ๐-th athlete as an integer ๐๐, where 1โค๐๐โค๐. All the strength values are different, that is, the array ๐ is a permutation of length ๐. We know that in a fight, if ๐๐>๐๐, then the ๐-th participant always wins the ๐-th.

The tournament goes like this: initially, all ๐ athletes line up in ascending order of their ids, and then there are infinitely many fighting rounds. In each round there is exactly one fight: the first two people in line come out and fight. The winner goes back to the front of the line, and the loser goes to the back.

Burenka decided to ask Tonya ๐ questions. In each question, Burenka asks how many victories the ๐-th participant gets in the first ๐ rounds of the competition for some given numbers ๐ and ๐. Tonya is not very good at analytics, so he asks you to help him answer all the questions.

Input
The first line contains one integer ๐ก (1โค๐กโค104) โ the number of test cases. Description of the test cases follows.

The first line of each test case contains two integers ๐ and ๐ (2โค๐โค105, 1โค๐โค105) โ the number of tournament participants and the number of questions.

The second line of each test case contains ๐ integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค๐) โ the array ๐, which is a permutation.

The next ๐ lines of a test case contain questions. Each line contains two integers ๐ and ๐ (1โค๐โค๐, 1โค๐โค109) โ the number of the participant and the number of rounds.

It is guaranteed that the sum of ๐ and the sum of ๐ over all test cases do not exceed 105.

Output
For each Burenka's question, print a single line containing one integer โ the answer to the question.
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
