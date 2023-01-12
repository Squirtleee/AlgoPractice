# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1779/submission/187885220
'''
Question Link: https://codeforces.com/contest/1779/problem/D

Boris thinks that chess is a tedious game. So he left his tournament early and went to a barber shop as his hair was a bit messy.

His current hair can be described by an array 𝑎1,𝑎2,…,𝑎𝑛, where 𝑎𝑖 is the height of the hair standing at position 𝑖. His desired haircut can be described by an array 𝑏1,𝑏2,…,𝑏𝑛 in a similar fashion.

The barber has 𝑚 razors. Each has its own size and can be used at most once. In one operation, he chooses a razor and cuts a segment of Boris's hair. More formally, an operation is:

Choose any razor which hasn't been used before, let its size be 𝑥;
Choose a segment [𝑙,𝑟] (1≤𝑙≤𝑟≤𝑛);
Set 𝑎𝑖:=min(𝑎𝑖,𝑥) for each 𝑙≤𝑖≤𝑟;
Notice that some razors might have equal sizes — the barber can choose some size 𝑥 only as many times as the number of razors with size 𝑥.

He may perform as many operations as he wants, as long as any razor is used at most once and 𝑎𝑖=𝑏𝑖 for each 1≤𝑖≤𝑛 at the end. He does not have to use all razors.

Can you determine whether the barber can give Boris his desired haircut?

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤20000). The description of the test cases follows.

The first line of each test case contains a positive integer 𝑛 (3≤𝑛≤2⋅105) — the length of arrays 𝑎 and 𝑏.

The second line of each test case contains 𝑛 positive integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109)  — Boris's current hair.

The third line of each test case contains 𝑛 positive integers 𝑏1,𝑏2,…,𝑏𝑛 (1≤𝑏𝑖≤109)  — Boris's desired hair.

The fourth line of each test case contains a positive integer 𝑚 (1≤𝑚≤2⋅105)  — the number of razors.

The fifth line of each test case contains 𝑚 positive integers 𝑥1,𝑥2,…,𝑥𝑚 (1≤𝑥𝑖≤109)  — the sizes of the razors.

It is guaranteed that the sum of 𝑛 and the sum of 𝑚 over all test cases do not exceed 2⋅105.

Output
For each test case, print "YES" if the barber can cut Boris's hair as desired. Otherwise, print "NO".
'''
'''
Sample Input:
7
3
3 3 3
2 1 2
2
1 2
6
3 4 4 6 3 4
3 1 2 3 2 3
3
3 2 3
10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
10
1 2 3 4 5 6 7 8 9 10
3
1 1 1
1 1 2
12
4 2 4 3 1 5 6 3 5 6 2 1
13
7 9 4 5 3 3 3 6 8 10 3 2 5
5 3 1 5 3 2 2 5 8 5 1 1 5
8
1 5 3 5 4 2 3 1
13
7 9 4 5 3 3 3 6 8 10 3 2 5
5 3 1 5 3 2 2 5 8 5 1 1 5
7
1 5 3 4 2 3 1
3
19747843 2736467 938578397
2039844 2039844 2039844
1
2039844
Sample Output:
YES
NO
YES
NO
YES
NO
YES
'''
import sys
from collections import Counter
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out='YES'
  hair=int(input())
  arr1=list(map(int,input().split()))
  arr2=list(map(int,input().split()))
  cut=int(input())
  razor=list(map(int,input().split()))
  razor.sort(reverse=True)
  for h in range(hair):
    if arr2[h]>arr1[h]:
      out='NO'
      break
  if out=='YES':
    cntr=Counter(razor)
    open=[]
    for h in range(hair):
      while len(open)>0 and open[-1]<arr2[h]:
        open.pop()
      if arr2[h]<arr1[h]:
        if open and arr2[h]==open[-1]:
          continue
        else:
          if arr2[h] in cntr and cntr[arr2[h]]>0:
            open.append(arr2[h])
            cntr[arr2[h]]-=1
          else:
            out='NO'
            break
  print(out)
