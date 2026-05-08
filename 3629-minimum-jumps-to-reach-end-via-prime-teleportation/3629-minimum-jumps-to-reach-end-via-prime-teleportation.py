from collections import *
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)

        spf = list(range(m + 1))
        for i in range(2, int(m ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        d = defaultdict(list)

        for i, x in enumerate(nums):
            t = x
            s = set()
            while t > 1:
                p = spf[t]
                s.add(p)
                while t % p == 0:
                    t //= p
            for p in s:
                d[p].append(i)

        q = deque([0])
        vis = {0}
        used = set()
        ans = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return ans

                for ni in [i - 1, i + 1]:
                    if 0 <= ni < n and ni not in vis:
                        vis.add(ni)
                        q.append(ni)

                x = nums[i]

                if x > 1 and spf[x] == x and x not in used:
                    used.add(x)
                    for j in d[x]:
                        if j not in vis:
                            vis.add(j)
                            q.append(j)

            ans += 1
        