# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1783/submission/188649373
'''
Question Link: https://codeforces.com/contest/1783/problem/C

You are participating in Yet Another Tournament. There are 𝑛+1 participants: you and 𝑛 other opponents, numbered from 1 to 𝑛.

Each two participants will play against each other exactly once. If the opponent 𝑖 plays against the opponent 𝑗, he wins if and only if 𝑖>𝑗.

When the opponent 𝑖 plays against you, everything becomes a little bit complicated. In order to get a win against opponent 𝑖, you need to prepare for the match for at least 𝑎𝑖 minutes — otherwise, you lose to that opponent.

You have 𝑚 minutes in total to prepare for matches, but you can prepare for only one match at one moment. In other words, if you want to win against opponents 𝑝1,𝑝2,…,𝑝𝑘, you need to spend 𝑎𝑝1+𝑎𝑝2+⋯+𝑎𝑝𝑘 minutes for preparation — and if this number is greater than 𝑚, you cannot achieve a win against all of these opponents at the same time.

The final place of each contestant is equal to the number of contestants with strictly more wins + 1. For example, if 3 contestants have 5 wins each, 1 contestant has 3 wins and 2 contestants have 1 win each, then the first 3 participants will get the 1-st place, the fourth one gets the 4-th place and two last ones get the 5-th place.

Calculate the minimum possible place (lower is better) you can achieve if you can't prepare for the matches more than 𝑚 minutes in total.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains two integers 𝑛 and 𝑚 (1≤𝑛≤5⋅105; 0≤𝑚≤∑𝑖=1𝑛𝑎𝑖) — the number of your opponents and the total time you have for preparation.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (0≤𝑎𝑖≤1000), where 𝑎𝑖 is the time you need to prepare in order to win against the 𝑖-th opponent.

It's guaranteed that the total sum of 𝑛 over all test cases doesn't exceed 5⋅105.

Output
For each test case, print the minimum possible place you can take if you can prepare for the matches no more than 𝑚 minutes in total.
'''
'''
Sample Input:
5
4 401
100 100 200 1
3 2
1 2 3
5 0
1 1 1 1 1
4 0
0 1 1 1
4 4
1 2 2 1
Sample Output:
1
2
6
4
1
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out=0
    length,time=map(int,input().split())
    arr=list(map(int,input().split()))
    pos={}
    for l in range(length):
        arr[l]=[arr[l],l]
        pos[l]=arr[l][0]
    win=0
    arr.sort()
    seen=set()
    oppo_won=set()
    for aa in range(length):
        a=arr[aa]
        if a[1] in seen:
            continue
        if aa<length-1 and time>=arr[aa][0] and time-arr[aa][0]<arr[aa+1][0] and arr[aa][1]!=win+1:
            if time>=pos[win+1] and win+1 not in seen:
                time-=pos[win+1]
                seen.add(win+1)
                win+=1
                oppo_won.add(a[1])
            else:
                win+=1
                time-=a[0]
        elif time>=a[0]:
            win+=1
            time-=a[0]
        else:
            oppo_won.add(a[1])
        seen.add(a[1])
    if win in oppo_won:
        print(length-win+1)
        
    else:
        print(max(length-win,1))
