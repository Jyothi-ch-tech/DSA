from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for u,v in edges:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)
        vis=set()
        def dfs(node):
            if node==destination:
                return True
            vis.add(node)
            for nei in graph[node]:
                if nei not in vis:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)