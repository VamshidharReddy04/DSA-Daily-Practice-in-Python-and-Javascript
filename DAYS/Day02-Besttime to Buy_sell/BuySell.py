# Array/stock problem you can buy and sell only once
# Given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    min_price=float('inf')  # initialize min price to infinity
    max_profit=0            # initialize max profit to 0
    for price in prices:
        # If the current price is less than the min price, update the min price
        if price<min_price:
            min_price=price
        # Calculate the profit that can be achieved by selling at the current price
        profit =price-min_price
        # If the calculated profit is greater than the max profit, update the max profit
        if profit>max_profit:
            max_profit=profit
    # Return the maximum profit
    return max_profit

# Test cases
print(maxProfit([7,1,5,3,6,4]))  # Output: 5
print(maxProfit([7,6,4,3,1]))    # Output: 0

# Brute Force Approach:O(n^2)
# Check every possible pair of buy and sell days to find the maximum profit.
# Optimal Approach:O(n)

# Time Complexity:O(n)
# Space Complexity:O(1)