# Time Limit per Test: 1 seconds
# Memory Limit per Test: 512 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1804/submission/197106073
'''
While James is gone on business, Vesper takes her time and explores what the legendary Casino Royale has to offer to people who are fond of competitive programming.

Her attention was grabbed by the very new "Pull Your Luck" roulette which functions in a pretty peculiar way. The roulette's wheel consists of 𝑛
 sectors number from 0
 to 𝑛−1
. There is no ball and the winning sector is determined by a static arrow pointing to one of the sectors. Sectors' indexes go in the natural order and the wheel always spins in the direction of indexes increment. That means that sector 𝑖+1
 goes right after sector 𝑖
 for all 𝑖
 from 0
 to 𝑛−2
, and sector 0
 goes right after sector 𝑛−1
.

After a bet is made, the player is allowed to pull the triggering handle herself and cause the wheel to spin. If the player's initial pull is made with the force equal to positive integer 𝑓
, the wheel will spin for 𝑓
 seconds. During the first second it will advance 𝑓
 sectors, the next second it will advance 𝑓−1
 sectors, then 𝑓−2
 sectors, and so on until it comes to a complete stop. After the wheel comes to a complete stop, the sector which the arrow is pointing to is the winning one.

The roulette's arrow currently points at sector 𝑥
. Vesper knows that she can pull the handle with any integer force from 1
 to 𝑝
 inclusive. Note that it is not allowed to pull the handle with force 0
, i. e. not pull it all. The biggest prize is awarded if the winning sector is 0
. Now Vesper wonders if she can make sector 0
 win by pulling the triggering handle exactly once?

Input
The first line of the input contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. Then follow 𝑡
 lines containing one test description each.

Each test description consists of three integers 𝑛
, 𝑥
 and 𝑝
 (3≤𝑛≤105
, 0≤𝑥<𝑛
, 1≤𝑝≤109
). They are the number of sectors on the wheel, the current sector the arrow points at, and the maximum force that Vesper can pull the handle with, respectively.

It is guaranteed that the sum of 𝑛
 over all test cases doesn't exceed 2⋅105
.

Output
Print 𝑡
 lines, the 𝑖
-th line should contain the answer for the 𝑖
-th test case. If it is possible to pull the handle with the integer force from 1
 to 𝑝
 in order to make sector 0
 win, print "Yes". Otherwise, print "No".
'''
'''
Sample Input:
7
5 2 1
5 2 2
10 0 100
11 7 100
3 1 1000
31 0 10
100 49 7
Sample Output:
No
Yes
Yes
Yes
No
No
No
'''
import sys 
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out=0
    length,cur,force=map(int,input().split())
    dist=length-cur
    dist%=length
    total=0
    ans='No'
    pos=[]
    per_cycle=-1
    for r in range(1,length+1):
        total+=r
        if r>force:
            break
        if total%length==dist:
            ans='Yes'
            break
        total%=length
        pos.append(total)
    
    if ans=='Yes':
        print(ans)
        continue
    per_cycle=pos[-1]
    if per_cycle==0:
        print('No')
        continue
    ind=0
    for p in pos:
        ind+=1
        if dist>p:
            diff=dist-p
            if diff%per_cycle==0:
                cyc=diff//per_cycle
                if cyc*(length)+ind<=force:
                    ans='Yes'
                    break
        else:
            diff=(length+dist)-p
            if diff%per_cycle==0:
                cyc=diff//per_cycle
                if cyc*(length)+ind<=force:
                    ans='Yes'
                    break
    
        
    print(ans)
