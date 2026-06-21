class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt=[0]*100001
        for i in costs:
            cnt[i]+=1
        ans=0
        for i in range(1,100001):
            k=min(cnt[i],coins//i)
            ans+=k
            coins-=k*i
        return ans
        