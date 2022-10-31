# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1735/submission/174572524
'''
Question Link: https://codeforces.com/contest/1735/problem/C

There was a string 𝑠 which was supposed to be encrypted. For this reason, all 26 lowercase English letters were arranged in a circle in some order, afterwards, each letter in 𝑠 was replaced with the one that follows in clockwise order, in that way the string 𝑡 was obtained.

You are given a string 𝑡. Determine the lexicographically smallest string 𝑠 that could be a prototype of the given string 𝑡.

A string 𝑎 is lexicographically smaller than a string 𝑏 of the same length if and only if:

in the first position where 𝑎 and 𝑏 differ, the string 𝑎 has a letter, that appears earlier in the alphabet than the corresponding letter in 𝑏.
Input
The first line of the input contains a single integer 𝑡 (1≤𝑡≤3⋅104) — the number of test cases. The description of test cases follows.

The first line of each test case contains one integer 𝑛 (1≤𝑛≤105) — the length of the string 𝑡.

The next line contains the string 𝑡 of the length 𝑛, containing lowercase English letters.

It is guaranteed that the sum of 𝑛 over all test cases doesn't exceed 2⋅105.

Output
For each test case, output a single line containing the lexicographically smallest string 𝑠 which could be a prototype of 𝑡.
'''
'''
Sample Input:
5
1
a
2
ba
10
codeforces
26
abcdefghijklmnopqrstuvwxyz
26
abcdefghijklmnopqrstuvwxzy

Sample Output:
b
ac
abcdebfadg
bcdefghijklmnopqrstuvwxyza
bcdefghijklmnopqrstuvwxyaz
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  length=int(input())
  word=input()
  word=[w for w in word]
  word.pop()
  out={}
  inward={}
  for k in range(26):
    out[chr(ord('a')+k)]=0
    inward[chr(ord('a')+k)]=0
  ans=""
  ll=0
  for w in word:
    if inward[w]!=0:
      ans+=inward[w]
    else:
      for j in range(26):
        char=chr(ord('a')+j)
        if w==char or out[char]!=0:
          continue
        cur=out[w]
        cnt=0
        while cnt<23 and cur!=0 and cur!=char:
          cnt+=1
          cur=out[cur]
        if char==cur:
          continue
        if cur==0 or cnt>=23:
          ans+=char
          inward[w]=char
          out[char]=w
          break
  print(ans)
