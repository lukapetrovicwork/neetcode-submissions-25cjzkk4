class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        best = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                best1 = prices[right] - prices[left]
                best = max(best, best1)
            else:
                left = right

            right += 1
            
        return best