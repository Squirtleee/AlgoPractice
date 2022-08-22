'''
Question Link: https://codeforces.com/contest/1709/problem/D

There is a grid, consisting of 𝑛 rows and 𝑚 columns. The rows are numbered from 1 to 𝑛 from bottom to top. The columns are numbered from 1 to 𝑚 from left to right. The 𝑖-th column has the bottom 𝑎𝑖 cells blocked (the cells in rows 1,2,…,𝑎𝑖), the remaining 𝑛−𝑎𝑖 cells are unblocked.

A robot is travelling across this grid. You can send it commands — move up, right, down or left. If a robot attempts to move into a blocked cell or outside the grid, it explodes.

However, the robot is broken — it executes each received command 𝑘 times. So if you tell it to move up, for example, it will move up 𝑘 times (𝑘 cells). You can't send it commands while the robot executes the current one.

You are asked 𝑞 queries about the robot. Each query has a start cell, a finish cell and a value 𝑘. Can you send the robot an arbitrary number of commands (possibly, zero) so that it reaches the finish cell from the start cell, given that it executes each command 𝑘 times?

The robot must stop in the finish cell. If it visits the finish cell while still executing commands, it doesn't count.

Input
The first line contains two integers 𝑛 and 𝑚 (1≤𝑛≤109; 1≤𝑚≤2⋅105) — the number of rows and columns of the grid.

The second line contains 𝑚 integers 𝑎1,𝑎2,…,𝑎𝑚 (0≤𝑎𝑖≤𝑛) — the number of blocked cells on the bottom of the 𝑖-th column.

The third line contains a single integer 𝑞 (1≤𝑞≤2⋅105) — the number of queries.

Each of the next 𝑞 lines contain five integers 𝑥𝑠,𝑦𝑠,𝑥𝑓,𝑦𝑓 and 𝑘 (𝑎[𝑦𝑠]<𝑥𝑠≤𝑛; 1≤𝑦𝑠≤𝑚; 𝑎[𝑦𝑓]<𝑥𝑓≤𝑛; 1≤𝑦𝑓≤𝑚; 1≤𝑘≤109) — the row and the column of the start cell, the row and the column of the finish cell and the number of times each your command is executed. The start and the finish cell of each query are unblocked.

Output
For each query, print "YES" if you can send the robot an arbitrary number of commands (possibly, zero) so that it reaches the finish cell from the start cell, given that it executes each command 𝑘 times. Otherwise, print "NO".
'''
'''
Sample Input:
11 10
9 0 0 10 3 4 8 11 10 8
6
1 2 1 3 1
1 2 1 3 2
4 3 4 5 2
5 3 11 5 3
5 3 11 5 2
11 9 9 10 1
Sample Output:
YES
NO
NO
NO
YES
YES
'''
'''
My Idea: Use sparse table to determine the maximum blocked column along the path and the minimum number of blocks the robot needs to move vertically.
'''

import math
 
# Fills lookup array lookup[][] in
# bottom up manner.
def buildSparseTable(arr, n):
 
    # Initialize M for the intervals
    # with length 1
    for i in range(0, n):
        lookup[i][0] = arr[i]
     
    j = 1
     
    # Compute values from smaller to
    # bigger intervals
    while (1 << j) <= n:
 
        # Compute minimum value for all
        # intervals with size 2^j
        i = 0
        while (i + (1 << j) - 1) < n:
 
            # For arr[2][10], we compare arr[lookup[0][7]]
            # and arr[lookup[3][10]]
            if (lookup[i][j - 1] >
                lookup[i + (1 << (j - 1))][j - 1]):
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = \
                        lookup[i + (1 << (j - 1))][j - 1]
             
            i += 1
        j += 1       
 
# Returns minimum of arr[L..R]
def qu(L, R):
 
    # Find highest power of 2 that is smaller
    # than or equal to count of elements in
    # given range. For [2, 10], j = 3
    j = int(math.log2(R - L + 1))
 
    # Compute minimum of last 2^j elements
    # with first 2^j elements in range.
    # For [2, 10], we compare arr[lookup[0][3]]
    # and arr[lookup[3][3]],
    if lookup[L][j] >= lookup[R - (1 << j) + 1][j]:
        return lookup[L][j]
 
    else:
        return lookup[R - (1 << j) + 1][j]
 
import sys
input = sys.stdin.readline
#rounds=int(input())
for ii in range(1):
    rows, cols = map(int, input().split())
    block = list(map(int, input().split()))
    length=len(block)
    # Driver Code
    if __name__ == "__main__":

      MAX = 20
        
      # lookup[i][j] is going to store minimum
      # value in arr[i..j]. Ideally lookup table
      # size should not be fixed and should be
      # determined using n Log n. It is kept
      # constant to keep code simple.
      lookup = [[0 for i in range(20)]
                 for j in range(2*10**5+1)]
      

      buildSparseTable(block,length)
    query = int(input())
    for q in range(query):
        out = 'YES'
        startr, startc, endr, endc, k = map(int, input().split())
        if abs(startr - endr) % k != 0 or abs(startc - endc) % k != 0:
            out = 'NO'
        if startc > endc:
            hold = startc
            startc = endc
            endc = hold
        big = 0
        if endc - 1 - startc >= 1:
            big = qu(startc,endc-1)
        else:
            big = 0
        if startr <= big and big<rows:
            move = (big-startr+1)
            if move // k != move / k:
                if k * (move // k + 1) > rows-startr:
                    out = 'NO'
        elif big==rows:
          out='NO'
        
        print(out)


