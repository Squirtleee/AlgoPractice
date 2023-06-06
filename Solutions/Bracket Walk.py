# Time Limit per Test: 3 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1838/submission/208649555
'''
Question Link: https://codeforces.com/contest/1838/problem/D

There is a string 𝑠
 of length 𝑛
 consisting of the characters '(' and ')'. You are walking on this string. You start by standing on top of the first character of 𝑠
, and you want to make a sequence of moves such that you end on the 𝑛
-th character. In one step, you can move one space to the left (if you are not standing on the first character), or one space to the right (if you are not standing on the last character). You may not stay in the same place, however you may visit any character, including the first and last character, any number of times.

At each point in time, you write down the character you are currently standing on. We say the string is walkable if there exists some sequence of moves that take you from the first character to the last character, such that the string you write down is a regular bracket sequence.

A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example, bracket sequences "()()", "(())" are regular (the resulting expressions are: "(1)+(1)", "((1+1)+1)"), and ")(" and "(" are not.

One possible valid walk on 𝑠=(())()))
. The red dot indicates your current position, and the red string indicates the string you have written down. Note that the red string is a regular bracket sequence at the end of the process.
You are given 𝑞
 queries. Each query flips the value of a character from '(' to ')' or vice versa. After each query, determine whether the string is walkable.

Queries are cumulative, so the effects of each query carry on to future queries.

Input
The first line of the input contains two integers 𝑛
 and 𝑞
 (1≤𝑛,𝑞≤2⋅105
) — the size of the string and the number of queries, respectively.

The second line of the input contains a string 𝑠
 of size 𝑛
, consisting of the characters '(' and ')' — the initial bracket string.

Each of the next 𝑞
 lines contains a single integer 𝑖
 (1≤𝑖≤𝑛
) — the index of the character to flip for that query.

Output
For each query, print "YES" if the string is walkable after that query, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
'''
'''
Sample Input:
10 9
(())()()))
9
7
2
6
3
6
7
4
8
Sample Output:
YES
YES
NO
NO
YES
NO
YES
NO
NO
'''

import sys

import bisect

 
class SortedList:
    class FenwickTree:
        def __init__(self, array):
            self.size = len(array)
            self.fen_tree = [0] * self.size
            for idx, val in enumerate(array):
                self.update(idx, val)
 
        def update(self, idx, delta):
            while idx < self.size:
                self.fen_tree[idx] += delta
                idx |= idx + 1
 
        def query(self, idx):
            res = 0
            while idx:
                res += self.fen_tree[idx - 1]
                idx &= idx - 1
            return res
 
        def find_kth(self, k):
            idx = -1
            for d in range(self.size.bit_length() - 1, -1, -1):
                right_idx = idx + (1 << d)
                if right_idx < self.size and k >= self.fen_tree[right_idx]:
                    idx = right_idx
                    k -= self.fen_tree[idx]
            return idx + 1, k
 
    def __init__(self, iterable=(), max_load=400):
        self.max_load = max_load
        self.size = 0
        self.lists = [[]]
        self.list_sizes = [0]
        self.min_values = []
        self.fenwick_tree = SortedList.FenwickTree([0])
        for value in iterable:
            self.insert(value)
 
    def insert(self, value):
        i = bisect.bisect_left(self.min_values, value)
        j = bisect.bisect_right(self.lists[i], value)
        self.lists[i].insert(j, value)
        self.size += 1
        self.list_sizes[i] += 1
        self.fenwick_tree.update(i, 1)
        if self.list_sizes[i] >= self.max_load:  # bucket full => split!
            first_half = self.lists[i][:self.max_load >> 1]
            second_half = self.lists[i][self.max_load >> 1:]
            self.lists[i:i + 1] = first_half, second_half
            self.list_sizes[i:i + 1] = len(first_half), len(second_half)
            self.min_values.insert(i, self.lists[i + 1][0])
            self.fenwick_tree = SortedList.FenwickTree(self.list_sizes)
 
    def remove(self, value):
        i = self.bisect_left(value)
        if 0 <= i < self.size and self[i] == value:
            self.pop(i)
 
    def _comp_internal_indices(self, index):
        if index < 0:
            index += self.size
        return self.fenwick_tree.find_kth(index)
 
    def pop(self, index=-1):
        i, j = self._comp_internal_indices(index)
        self.size -= 1
        self.list_sizes[i] -= 1
        self.fenwick_tree.update(i, -1)
        return self.lists[i].pop(j)
 
    def __len__(self):
        return self.size
 
    def __getitem__(self, k):
        i, j = self._comp_internal_indices(k)
        return self.lists[i][j]
 
    def __iter__(self):
        return (item for lst in self.lists for item in lst)
 
    def bisect_left(self, x):
        i = bisect.bisect_left(self.min_values, x)
        return self.fenwick_tree.query(i) + bisect.bisect_left(self.lists[i], x)
 
    def bisect_right(self, x):
        i = bisect.bisect_right(self.min_values, x)
        return self.fenwick_tree.query(i) + bisect.bisect_right(self.lists[i], x)
 
    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)
 
    def __contains__(self, x):
        return self.count(x) > 0

input = sys.stdin.readline
#rounds = int(input())
for ii in range(1):
  out=0
  length,query=map(int,input().split())
  seq=input()
  seq=[s for s in seq]
  bad=SortedList(max_load=200)
  for l in range(length):
    if l%2==0 and seq[l]==')':
      bad.insert(l)
    elif l%2==1 and seq[l]=='(':
      bad.insert(l)
  
  
  
  for q in range(query):
    move=int(input())
    move-=1
    if length%2==1:
      print('NO')
    else:
      if seq[move]=='(':
        seq[move]=')'
        if move%2==1:
          bad.remove(move)
        else:
          bad.insert(move)
      else:
        seq[move]='('
        if move%2==0:
          bad.remove(move)
        else:
          bad.insert(move)
      #print(bad[0],bad[-1],seq,move)
      if bad.size==0:
        print("YES")
      elif  (bad[0]%2==0 or bad[-1]%2==1):
        
        print('NO')
      else:
        print("YES")
      
