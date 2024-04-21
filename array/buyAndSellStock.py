# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# [3,2,6,5,0,3]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        numDays = len(prices)
        
        for i in range(1, numDays):
            # If the price today is higher than yesterday, we can sell for profit
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        
        return maxProfit
    
# Notes:
# don't need to simulate real-life (i.e. don't overcomplicate it)
# don't be afraid to use whatever shortcut is available to solve the problem
# buy and sell on same day means you just need to find thr difference between tdy and yesterday's price
