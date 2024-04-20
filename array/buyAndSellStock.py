# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# [3,2,6,5,0,3]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0;
        numDays = len(prices)
        for startIdx in range(numDays):
            profit = 0
            myStock = prices[startIdx]
            hasStock = True
            for i in range(startIdx + 1, numDays):
                priceToday = prices[i]
                priceTmr = -1
                if i+1 < numDays:
                    priceTmr = prices[i+1]
                if hasStock:
                    if priceToday > myStock:
                        profit += priceToday - myStock
                        myStock = -1
                        hasStock = False
                
                if(priceTmr > priceToday and not hasStock):
                    myStock = priceToday
                    hasStock = True

            if profit > maxProfit:
                maxProfit = profit
        return maxProfit