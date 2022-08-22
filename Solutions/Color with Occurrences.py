# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1714/submission/166646314
'''
Question Link: https://codeforces.com/contest/1714/problem/D

You are given some text 𝑡 and a set of 𝑛 strings 𝑠1,𝑠2,…,𝑠𝑛.

In one step, you can choose any occurrence of any string 𝑠𝑖 in the text 𝑡 and color the corresponding characters of the text in red. For example, if 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊 and 𝑠1=𝚋𝚊, 𝑠2=𝚊𝚋𝚊, you can get 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊, 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊 or 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊 in one step.

You want to color all the letters of the text 𝑡 in red. When you color a letter in red again, it stays red.

In the example above, three steps are enough:

Let's color 𝑡[2…4]=𝑠2=𝚊𝚋𝚊 in red, we get 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊;
Let's color 𝑡[1…2]=𝑠1=𝚋𝚊 in red, we get 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊;
Let's color 𝑡[4…6]=𝑠2=𝚊𝚋𝚊 in red, we get 𝑡=𝚋𝚊𝚋𝚊𝚋𝚊.
Each string 𝑠𝑖 can be applied any number of times (or not at all). Occurrences for coloring can intersect arbitrarily.

Determine the minimum number of steps needed to color all letters 𝑡 in red and how to do it. If it is impossible to color all letters of the text 𝑡 in red, output -1.

Input
The first line of the input contains an integer 𝑞 (1≤𝑞≤100) —the number of test cases in the test.

The descriptions of the test cases follow.

The first line of each test case contains the text 𝑡 (1≤|𝑡|≤100), consisting only of lowercase Latin letters, where |𝑡| is the length of the text 𝑡.

The second line of each test case contains a single integer 𝑛 (1≤𝑛≤10) — the number of strings in the set.

This is followed by 𝑛 lines, each containing a string 𝑠𝑖 (1≤|𝑠𝑖|≤10) consisting only of lowercase Latin letters, where |𝑠𝑖| — the length of string 𝑠𝑖.

Output
For each test case, print the answer on a separate line.

If it is impossible to color all the letters of the text in red, print a single line containing the number -1.

Otherwise, on the first line, print the number 𝑚 — the minimum number of steps it will take to turn all the letters 𝑡 red.

Then in the next 𝑚 lines print pairs of indices: 𝑤𝑗 and 𝑝𝑗 (1≤𝑗≤𝑚), which denote that the string with index 𝑤𝑗 was used as a substring to cover the occurrences starting in the text 𝑡 from position 𝑝𝑗. The pairs can be output in any order.

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
