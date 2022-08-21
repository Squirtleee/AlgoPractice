# Knapsack Size:2000000
# Data Size: 2000

f = open("/Users/jesshuang/Desktop/CS/Courses/DP/knapData2.txt", "r")
cargo=[]
for x in f:
    value,size=map(int,x.split())
    cargo.append((value,size))

now=[]
before=[]
for r in range(1):
    hold=[0]*2000001
before=hold
    

for x in range(1,2001):
    now=[0]*2000001
    cur_cargo=cargo[x-1]
    for y in range(1,2000001):
        if cur_cargo[1]>y:
            now[y]=before[y]
        else:
            now[y]=max(before[y],cur_cargo[0]+before[y-cur_cargo[1]])
    before=now
print(now[-1])
