# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1702/submission/163670293
'''
Question Link: https://codeforces.com/contest/1702/problem/C

Along the railroad there are stations indexed from 1 to 109. An express train always travels along a route consisting of π stations with indices π’1,π’2,β¦,π’π, where (1β€π’πβ€109). The train travels along the route from left to right. It starts at station π’1, then stops at station π’2, then at π’3, and so on. Station π’π β the terminus.

It is possible that the train will visit the same station more than once. That is, there may be duplicates among the values π’1,π’2,β¦,π’π.

You are given π queries, each containing two different integers ππ and ππ (1β€ππ,ππβ€109). For each query, determine whether it is possible to travel by train from the station with index ππ to the station with index ππ.

For example, let the train route consist of 6 of stations with indices [3,7,1,5,1,4] and give 3 of the following queries:

π1=3, π1=5
It is possible to travel from station 3 to station 5 by taking a section of the route consisting of stations [3,7,1,5]. Answer: YES.

π2=1, π2=7
You cannot travel from station 1 to station 7 because the train cannot travel in the opposite direction. Answer: NO.

π3=3, π3=10
It is not possible to travel from station 3 to station 10 because station 10 is not part of the train's route. Answer: NO.

Input
The first line of the input contains an integer π‘ (1β€π‘β€104) βthe number of test cases in the test.

The descriptions of the test cases follow.

The first line of each test case is empty.

The second line of each test case contains two integers: π and π (1β€πβ€2β105,1β€πβ€2β105) βthe number of stations the train route consists of and the number of queries.

The third line of each test case contains exactly π integers π’1,π’2,β¦,π’π (1β€π’πβ€109). The values π’1,π’2,β¦,π’π are not necessarily different.

The following π lines contain two different integers ππ and ππ (1β€ππ,ππβ€109) describing the query with index π.

It is guaranteed that the sum of π values over all test cases in the test does not exceed 2β105. Similarly, it is guaranteed that the sum of π values over all test cases in the test also does not exceed 2β105
Output
For each test case, output on a separate line:

YES, if you can travel by train from the station with index ππ to the station with index ππ
NO otherwise.
You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).
'''
'''
Sample Input:
3


6 3
3 7 1 5 1 4
3 5
1 7
3 10


3 3
1 2 1
2 1
1 2
4 5


7 5
2 1 1 1 2 4 4
1 3
1 4
2 1
4 1
1 2
Sample Output:
YES
NO
NO
YES
YES
NO
NO
YES
YES
NO
YES
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  _ = input()
  n, k = map(int, input().split())
  u = list(map(int, input().split()))
  def back():
    return [-5,-5]
  w = defaultdict(back)
  for o in range(n):
      ind=u[o]
      ind=ind/10
      if w[ind][0]!=-5:
          w[ind][1] = o
      else:
          w[ind] = [o, o]
  for s in range(k):
      a, b = map(int, input().split())
      a=a/10
      b=b/10
      if w[a][0] <= w[b][1] and w[a][0]!=-5:
          print("YES")
      else:
          print("NO")
