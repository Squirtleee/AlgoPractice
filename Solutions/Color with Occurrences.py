# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1714/submission/166646314
'''
Question Link: https://codeforces.com/contest/1714/problem/D

You are given some text π‘ and a set of π strings π 1,π 2,β¦,π π.

In one step, you can choose any occurrence of any string π π in the text π‘ and color the corresponding characters of the text in red. For example, if π‘=ππππππ and π 1=ππ, π 2=πππ, you can get π‘=ππππππ, π‘=ππππππ or π‘=ππππππ in one step.

You want to color all the letters of the text π‘ in red. When you color a letter in red again, it stays red.

In the example above, three steps are enough:

Let's color π‘[2β¦4]=π 2=πππ in red, we get π‘=ππππππ;
Let's color π‘[1β¦2]=π 1=ππ in red, we get π‘=ππππππ;
Let's color π‘[4β¦6]=π 2=πππ in red, we get π‘=ππππππ.
Each string π π can be applied any number of times (or not at all). Occurrences for coloring can intersect arbitrarily.

Determine the minimum number of steps needed to color all letters π‘ in red and how to do it. If it is impossible to color all letters of the text π‘ in red, output -1.

Input
The first line of the input contains an integer π (1β€πβ€100) βthe number of test cases in the test.

The descriptions of the test cases follow.

The first line of each test case contains the text π‘ (1β€|π‘|β€100), consisting only of lowercase Latin letters, where |π‘| is the length of the text π‘.

The second line of each test case contains a single integer π (1β€πβ€10) β the number of strings in the set.

This is followed by π lines, each containing a string π π (1β€|π π|β€10) consisting only of lowercase Latin letters, where |π π| β the length of string π π.

Output
For each test case, print the answer on a separate line.

If it is impossible to color all the letters of the text in red, print a single line containing the number -1.

Otherwise, on the first line, print the number π β the minimum number of steps it will take to turn all the letters π‘ red.

Then in the next π lines print pairs of indices: π€π and ππ (1β€πβ€π), which denote that the string with index π€π was used as a substring to cover the occurrences starting in the text π‘ from position ππ. The pairs can be output in any order.

If there are several answers, output any of them.
'''
'''
Sample Input:
1
bababa
2
ba
aba
Sample Output:
3
2 2
1 1
2 4
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  string=input()
  string=[s for s in string]
  string.pop(-1)
  options=int(input())
  sub=[]
  dp=[]
  for _ in range(len(string)):
    dp.append([0,0])
  for o in range(options):
    text=input()
    text=[t for t in text]
    text.pop(-1)
    for y in range(len(string)-len(text)+1):
      if text==string[y:y+len(text)]:
        if dp[y][0]<y+len(text):
          dp[y][0]=y+len(text)
          dp[y][1]=o+1
  
  ans=[]
  start=0
  ind=dp[0][1]
  ans.append([str(ind),str(start+1)])
  nope=False
  while dp[start][0]<len(string) and nope==False:
    ori=start
    for u in range(dp[start][0]+1):
      if dp[u][0]>dp[start][0]:
        start=u
        ind=dp[u][1]
    if ori==start:
      nope=True
      break
    else:
      ans.append([str(ind),str(start+1)])
  if nope:
    print(-1)
  else:
    print(len(ans))
    for a in ans:
      print(' '.join(a))
