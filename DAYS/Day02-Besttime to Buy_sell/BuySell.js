//  Example:
//  Input: prices = [7,1,5,3,6,4]
//  Output: 5
//  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//  Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


function maxProfit(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    for (let price of prices) {
        if (price < minPrice)
            minPrice = price;
        let profit = price - minPrice;
        if (profit > maxProfit) maxProfit = profit
    }
    return maxProfit
}

console.log(maxProfit([7,1,5,3,6,4])); // 5
console.log(maxProfit([7,6,4,3,1])); // 0

// Time Complexity: O(n) where n is the number of days (length of prices array)
// Space Complexity: O(1) as we are using only constant space