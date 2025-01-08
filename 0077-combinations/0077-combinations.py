class Solution(object):
    def combine(self, n, k):
        res = []

        def dfs(elements, start, k):
            if k == 0:
                res.append(elements[:])
                return
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([],1,k)
        return res