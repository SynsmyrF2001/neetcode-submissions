class Solution {
    public int maxProfit(int[] prices) {
        // Pattern:  Greedy/One Pass tracking 
        // To maximize prices[j] - prices[i] where j > i, for every price on day j, we want to subtract the minimum price encountered so far before day j
        // We can maintain a running minimum minPrice as we traverse the array
        // At each step, calculate the potential profit prices[j] - minPrice and update maxProfit
        /* Track the lowest price seen so fat (minPrice). For each price, determine the profit if sold today, update maxProfit, and update minPrice */
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }
}
