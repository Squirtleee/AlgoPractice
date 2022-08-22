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
        for sh in shifts:
            start=sh[0]
            end=sh[1]
            direction=sh[2]
            if direction==0:
                change[start]-=1
                if end+1<len(s):
                    change[end+1]+=1
            else:
                change[start]+=1
                if end+1<len(s):
                    change[end+1]-=1
        plus=0
        for l in range(len(s)):
            num=ord(s[l])
            plus+=change[l]
            if plus<0:
                plus=(abs(plus)%26)*-1
            else:
                plus%=26
            num+=plus
            if num<97:
                num+=26
            elif num>122:
                num-=26
            s[l]=chr(num)
        return ''.join(s)
