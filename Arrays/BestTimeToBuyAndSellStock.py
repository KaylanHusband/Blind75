class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Approach: Dynamic Programming + memoization - The max profit will be given by the max difference, 
        to find this we need to track the minimuim seen of all values to the current point. 
        The maximum will be the largest difference observed after the iteration is complete
        Complexity Analysis:
        Time: O(n)
        Space: O(1)
        """
        minSeen = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(price-minSeen, maxProfit)
            minSeen = min(price, minSeen)
        
        return maxProfit