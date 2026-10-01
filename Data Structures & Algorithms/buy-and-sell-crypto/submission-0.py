class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        steps
        -> if price.length is 0 then return 0
        1. Set buying as first price
        2. set profit = 0
        3. for loop -> starting i =1, end = i < lenght of array
        4. Check if next price less than current ( update ), else remain
        5. if next price gt buying price, find CurrentProfit
        6. get the maximum of (profit, CurrentProfit)
        7. Return profit  

        Time: O(n)
        Space: O(1)


        step 2
        1. pointer( selling, buying )
        2. Mprofit = 0
        3. loop until selling is less then array size
        4. check ( is selling gt buying)
            profit (s-b)
            Mprofit ( profit, Mprofit)
            else 
            selling price = buying
        
        return Mprofix

        time comp: 

        """

        if len(prices) == 0:
            return 0
            
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1

        return max_profit
        
        