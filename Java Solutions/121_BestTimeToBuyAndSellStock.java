class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int lowest = prices[0];
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < lowest) {
                lowest = prices[i];
            } else if (prices[i] - lowest > res) {
                res = prices[i] - lowest;
            }
        }
        return res;
    }
}