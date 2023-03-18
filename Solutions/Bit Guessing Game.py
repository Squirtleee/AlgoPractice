# Time Limit per Test: 1 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1780/submission/190705491
'''
Quesiton Link: https://codeforces.com/contest/1780/problem/D

This is an interactive problem.

Kira has a hidden positive integer 𝑛
, and Hayato needs to guess it.

Initially, Kira gives Hayato the value cnt
 — the number of unit bits in the binary notation of 𝑛
. To guess 𝑛
, Hayato can only do operations of one kind: choose an integer 𝑥
 and subtract it from 𝑛
. Note that after each operation, the number 𝑛
 changes. Kira doesn't like bad requests, so if Hayato tries to subtract a number 𝑥
 greater than 𝑛
, he will lose to Kira. After each operation, Kira gives Hayato the updated value cnt
 — the number of unit bits in the binary notation of the updated value of 𝑛
.

Kira doesn't have much patience, so Hayato must guess the original value of 𝑛
 after no more than 30
 operations.

Since Hayato is in elementary school, he asks for your help. Write a program that guesses the number 𝑛
. Kira is an honest person, so he chooses the initial number 𝑛
 before all operations and does not change it afterward.

Input
The input data contains several test cases. The first line contains one integer 𝑡
 (1≤𝑡≤500
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains the number cnt
 — the initial number of unit bits in the binary notation 𝑛
.

The hidden integer 𝑛
 satisfies the following constraint: 1≤𝑛≤109
.

Interaction
To guess 𝑛
, you can perform the operation at most 30
 times. To do that, print a line with the following format: "- x" (1≤𝑥≤109
).

After this operation, the number 𝑥
 is subtracted from 𝑛
, and therefore 𝑛
 is changed. If the number 𝑥
 is greater than the current value of 𝑛
, then the request is considered invalid.

After the operation read a line containing a single non-negative integer cnt
 — the number of unit bits in the binary notation of the current 𝑛
 after the operation.

When you know the initial value of 𝑛
, print one line in the following format: "! n" (1≤𝑛≤109
).

After that, move on to the next test case, or terminate the program if there are none.
'''
'''
Sample Input:
3

1

0

1

1

0

2

1

0
Sample Output:
- 1

! 1

- 1

- 1

! 2

- 2

- 1

! 3
'''
import sys
input = sys.stdin.readline
rounds = int(input())
for ii in range(rounds):
  out=0
  last=0
  ones=int(input())
  ans=[0]*(31)
  for cycle in range(30):
    print('-',2**cycle-last,flush=True)
    res=int(input())
    if res==ones-1:
      ans[cycle]=1
      ones-=1
      last=0
    else:
      last=2**cycle
    if ones==0:
      break
  for k in range(31):
    if ans[k]==0:
      continue
    out+=2**k
  print('!',out,flush=True)

