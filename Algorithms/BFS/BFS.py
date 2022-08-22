'''
Quesiton Link: https://leetcode.com/contest/biweekly-contest-81/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
Return the number of pairs of different nodes that are unreachable from each other.
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        out=0
        path=[]
        for m in range(n):
            path.append(set())
        for e in edges:
            path[e[0]].add(e[1])
            path[e[1]].add(e[0])
        visited=set()
        start=0
        while len(visited)<n:
            stack=deque()
            cluster=set()
            while start in visited:
                start+=1
            stack.append(start)
            while stack:
                current=stack.popleft()
                cluster.add(current)
                for node in path[current]:
                    if node not in cluster:
                        stack.append(node)
            for c in cluster:
                visited.add(c)
            out+=(len(cluster)*(n-len(cluster)))
        return out//2
