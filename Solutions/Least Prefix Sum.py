# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1779/submission/187871698
'''
Question Link: https://codeforces.com/contest/1779/problem/C

Baltic, a famous chess player who is also a mathematician, has an array 𝑎1,𝑎2,…,𝑎𝑛, and he can perform the following operation several (possibly 0) times:

Choose some index 𝑖 (1≤𝑖≤𝑛);
multiply 𝑎𝑖 with −1, that is, set 𝑎𝑖:=−𝑎𝑖.
Baltic's favorite number is 𝑚, and he wants 𝑎1+𝑎2+⋯+𝑎𝑚 to be the smallest of all non-empty prefix sums. More formally, for each 𝑘=1,2,…,𝑛 it should hold that
𝑎1+𝑎2+⋯+𝑎𝑘≥𝑎1+𝑎2+⋯+𝑎𝑚.
Please note that multiple smallest prefix sums may exist and that it is only required that 𝑎1+𝑎2+⋯+𝑎𝑚 is one of them.

Help Baltic find the minimum number of operations required to make 𝑎1+𝑎2+⋯+𝑎𝑚 the least of all prefix sums. It can be shown that a valid sequence of operations always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤10000). The description of the test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 (1≤𝑚≤𝑛≤2⋅105) — the size of Baltic's array and his favorite number.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (−109≤𝑎𝑖≤109) — the array.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, print a single integer — the minimum number of required operations.
'''
'''
Sample Input:
6
4 3
-1 -2 -3 -4
4 3
1 2 3 4
1 1
1
5 5
-2 3 -5 1 -20
5 2
-2 3 -5 -5 -20
10 4
345875723 -48 384678321 -375635768 -35867853 -35863586 -358683842 -81725678 38576 -357865873
Sample Output:
1
1
0
0
3
4
'''
import sys
import heapq
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
    out=0
    length,fav=map(int,input().split())
    arr=list(map(int,input().split()))
    h=[]
    heapq.heapify(h)
    total=0
    for m in range(fav,length):
        total+=arr[m]
        heapq.heappush(h,arr[m])
        if total<0:
            cur=heapq.heappop(h)
            total-=2*cur
            out+=1
    total=0
    h=[]
    heapq.heapify(h)
    if fav>1:
        for y in range(fav-1,0,-1):
            total+=arr[y]
            heapq.heappush(h,-arr[y])
            while total>0:
                cur=heapq.heappop(h)
                total+=2*cur
                out+=1
    print(out)
