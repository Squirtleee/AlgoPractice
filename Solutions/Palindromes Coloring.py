# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1624/submission/164976405	
'''
Question Link: https://codeforces.com/contest/1624/problem/D

You have a string 𝑠 consisting of lowercase Latin alphabet letters.

You can color some letters in colors from 1 to 𝑘. It is not necessary to paint all the letters. But for each color, there must be a letter painted in that color.

Then you can swap any two symbols painted in the same color as many times as you want.

After that, 𝑘 strings will be created, 𝑖-th of them will contain all the characters colored in the color 𝑖, written in the order of their sequence in the string 𝑠.

Your task is to color the characters of the string so that all the resulting 𝑘 strings are palindromes, and the length of the shortest of these 𝑘 strings is as large as possible.

Read the note for the first test case of the example if you need a clarification.

Recall that a string is a palindrome if it reads the same way both from left to right and from right to left. For example, the strings abacaba, cccc, z and dxd are palindromes, but the strings abab and aaabaa — are not.

Input
The first line of input data contains a single integer 𝑡 (1≤𝑡≤104) — the number of input data sets in the test.

The descriptions of the input data sets follow.

The first line of the description of each input data set contains two integers 𝑛 and 𝑘 (1≤𝑘≤𝑛≤2⋅105) — the length of the string and the number of colors in which its letters can be painted. The second line of the description of each input data set contains a string 𝑠 of length 𝑛 consisting of lowercase letters of the Latin alphabet.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each set of input data, output a single integer  — the maximum length of the shortest palindrome string that can be obtained.
'''
'''
Sample Input:
10
8 2
bxyaxzay
6 3
aaaaaa
6 1
abcdef
6 6
abcdef
3 2
dxd
11 2
abcabcabcac
6 6
sipkic
7 2
eatoohd
3 1
llw
6 2
bfvfbv
Sample Output:
3
2
1
1
1
5
1
1
3
3
'''
import sys
from collections import Counter
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  length,colors=map(int,input().split())
  letters=input()
  letters=[o for o in letters]
  letters.pop(-1)
  cnt=Counter(letters)
  seq=[0]*colors
  
  for c in cnt:
    while cnt[c]>1:
      for g in range(colors):
        seq[g]+=2
        cnt[c]-=2
        if cnt[c]<2:
          break
    seq.sort()
  q=2
  ind=0
  for cn in cnt:
    if cnt[cn]==1:
        seq[ind]+=1
        ind+=1
    if ind>=colors:
      break
  if max(seq)-min(seq)>=2:
    small=seq.count(min(seq))
    big=seq.count(max(seq))
    if big>=small and max(seq)%2==0 and min(seq)%2==0:
      print(min(seq)+1)
    else:
      print(min(seq))
  else:
    print(min(seq))
