'''
Question Link: https://codeforces.com/contest/1701/problem/C

There are ๐ workers and ๐ tasks. The workers are numbered from 1 to ๐. Each task ๐ has a value ๐๐ โ the index of worker who is proficient in this task.

Every task should have a worker assigned to it. If a worker is proficient in the task, they complete it in 1 hour. Otherwise, it takes them 2 hours.

The workers work in parallel, independently of each other. Each worker can only work on one task at once.

Assign the workers to all tasks in such a way that the tasks are completed as early as possible. The work starts at time 0. What's the minimum time all tasks can be completed by?

Input
The first line contains a single integer ๐ก (1โค๐กโค104) โ the number of testcases.

The first line of each testcase contains two integers ๐ and ๐ (1โค๐โค๐โค2โ105) โ the number of workers and the number of tasks.

The second line contains ๐ integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค๐) โ the index of the worker proficient in the ๐-th task.

The sum of ๐ over all testcases doesn't exceed 2โ105.

Output
For each testcase, print a single integer โ the minimum time all tasks can be completed by.
'''
'''
Sample Input:
4
2 4
1 2 1 2
2 4
1 1 1 1
5 5
5 1 3 2 4
1 1
1
Sample Output:
2
3
1
1
'''
'''
My Idea: Binary search for the minimum time. If at current time the workers can complete equal to or more than the required tasks, than set the upper boundary to current time. If at current time the workers can complete less than the required tasks, than set the lower boundary to current time +1.
'''
import sys
input = sys.stdin.readline
rounds=int(input())
for ii in range(rounds):
  out=0
  worker,length=map(int,input().split())
  arr=list(map(int,input().split()))
  pro=[0]*worker
  for l in range(length):
    pro[arr[l]-1]+=1
  upper=2*length+1
  lower=length//worker
  while upper>lower:
    time=(lower+upper)//2
    done=0
    for ll in range(worker):
      if pro[ll]>=time:
        done+=time
      else:
        done+=(pro[ll]+(time-pro[ll])//2)
    if done>=length:
      upper=time
    else:
      lower=time+1
  print(upper)
