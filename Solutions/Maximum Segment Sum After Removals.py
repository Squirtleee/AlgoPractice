'''
Question Link: https://leetcode.com/problems/maximum-segment-sum-after-removals/

You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.

A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.

Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.

Note: The same index will not be removed more than once.
'''
'''
Example:
Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
Output: [14,7,2,2,0]
'''
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        data={}
        removeQueries.pop(0)
        removeQueries=removeQueries[::-1]
        ans=[0]
        cur=0
        for r in removeQueries:
            data[r]=[nums[r],1]
            lengthr=0
            lengthl=0
            sumr=0
            suml=0
            if r+1 in data:
                lengthr=data[r+1][1]
                sumr=data[r+1][0]
            if r-1 in data:
                lengthl=data[r-1][1]
                suml=data[r-1][0]
            total=nums[r]+suml+sumr
            data[r+lengthr]=[total,lengthr+lengthl+1]
            data[r-lengthl]=[total,lengthr+lengthl+1]
            cur=max(cur,total)
            ans.insert(0,cur)
        return ans
