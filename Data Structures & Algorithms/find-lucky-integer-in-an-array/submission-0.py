class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        ans = -1

        for n, count in freq.items():
            if n == count:
                ans = max(ans,n)

        return ans