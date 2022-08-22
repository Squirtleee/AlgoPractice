# Time Limit per Test: 2 seconds
# Memory Limit per Test: 256 megabytes
# Using: PyPy 3-64
# Solution Link: https://codeforces.com/contest/1714/submission/166590530
'''
Question Link: https://codeforces.com/contest/1714/problem/E

You are given an array of 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛
You can apply the following operation an arbitrary number of times:

select an index 𝑖 (1≤𝑖≤𝑛) and replace the value of the element 𝑎𝑖 with the value 𝑎𝑖+(𝑎𝑖mod10), where 𝑎𝑖mod10 is the remainder of the integer dividing 𝑎𝑖 by 10.
For a single index (value 𝑖), this operation can be applied multiple times. If the operation is applied repeatedly to the same index, then the current value of 𝑎𝑖 is taken into account each time. For example, if 𝑎𝑖=47 then after the first operation we get 𝑎𝑖=47+7=54, and after the second operation we get 𝑎𝑖=54+4=58.

Check if it is possible to make all array elements equal by applying multiple (possibly zero) operations.

For example, you have an array [6,11].

Let's apply this operation to the first element of the array. Let's replace 𝑎1=6 with 𝑎1+(𝑎1mod10)=6+(6mod10)=6+6=12. We get the array [12,11].
Then apply this operation to the second element of the array. Let's replace 𝑎2=11 with 𝑎2+(𝑎2mod10)=11+(11mod10)=11+1=12. We get the array [12,12].
Thus, by applying 2 operations, you can make all elements of an array equal.

Input
The first line contains one integer 𝑡 (1≤𝑡≤104) — the number of test cases. What follows is a description of each test case.

The first line of each test case contains one integer 𝑛 (1≤𝑛≤2⋅105) — the size of the array.

The second line of each test case contains 𝑛 integers 𝑎𝑖 (0≤𝑎𝑖≤109) — array elements.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case print:

YES if it is possible to make all array elements equal;
NO otherwise.
You can print YES and NO in any case (for example, the strings yEs, yes, Yes and YES will be recognized as a positive answer) .
'''
'''
Sample Input:
10
2
6 11
3
2 18 22
5
5 10 5 10 5
4
1 2 4 8
2
4 5
3
93 96 102
2
40 6
2
50 30
2
22 44
2
1 5
Sample Output:
Yes
No
Yes
Yes
No
Yes
No
No
Yes
No
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
    out='Yes'
    length=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    for l in range(length-1):
        if arr[l]==arr[l+1]:
            continue
        if arr[l]>arr[l+1]:
            hold=arr[l]
            arr[l]=arr[l+1]
            arr[l+1]=hold
        if arr[l]%2==1:
            arr[l]+=arr[l]%10
        if arr[l]%10>0:
            diff=arr[l+1]-arr[l]
            arr[l]+=(diff//20)*20
            diff=diff%20
        if arr[l]==arr[l+1]:
            continue
        cnt=0
        while arr[l]!=arr[l+1] and cnt<6 and arr[l]%10>0:
            while arr[l]<arr[l+1]:
                arr[l]+=arr[l]%10
            while arr[l+1]<arr[l]:
                arr[l+1]+=arr[l+1]%10
                cnt+=1
                if arr[l+1]%10==0:
                    cnt=9
                    break
        if arr[l]!=arr[l+1]:
            out='No'
            break
    print(out)
