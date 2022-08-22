'''
Question Link: https://leetcode.com/contest/biweekly-contest-85/problems/shifting-letters-ii/

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.
'''
'''
Example:
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s=[p for p in s]
        change=[0]*len(s)
        half=(len(s))//2
        total=0
        for k in shifts:
            start=k[0]
            end=k[1]
            direction=k[2]
            if end-start+1<half:
                if direction==0:
                    for y in range(start,end+1):
                        change[y]-=1
                        if change[y]<0:
                            change[y]=(abs(change[y])%26)*-1
                        else:
                            change[y]=change[y]%26
                else:
                    for y in range(start,end+1):
                        change[y]+=1
                        if change[y]<0:
                            change[y]=(abs(change[y])%26)*-1
                        else:
                            change[y]=change[y]%26
            else:
                if direction==0:
                    total-=1
                    if total<0:
                        total=(abs(total)%26)*-1
                    else:
                        total%=26
                    for u in range(0,start):
                        change[u]+=1
                        if change[u]<0:
                            change[u]=(abs(change[u])%26)*-1
                        else:
                            change[u]=change[u]%26
                    for p in range(end+1,len(s)):
                        change[p]+=1
                        if change[p]<0:
                            change[p]=(abs(change[p])%26)*-1
                        else:
                            change[p]=change[p]%26
                else:
                    total+=1
                    if total<0:
                        total=(abs(total)%26)*-1
                    else:
                        total%=26
                    for u in range(0,start):
                        change[u]-=1
                        if change[u]<0:
                            change[u]=(abs(change[u])%26)*-1
                        else:
                            change[u]=change[u]%26
                    for p in range(end+1,len(s)):
                        change[p]-=1
                        if change[p]<0:
                            change[p]=(abs(change[p])%26)*-1
                        else:
                            change[p]=change[p]%26
        for l in range(len(s)):
            change[l]+=total
            if change[l]<0:
                change[l]=(abs(change[l])%26)*-1
            else:
                change[l]=change[l]%26
            num=ord(s[l])
            num+=change[l]
            if num<97:
                num+=26
            elif num>122:
                num-=26
            s[l]=chr(num)
        return (''.join(s))
