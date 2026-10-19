class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0){
            return 0;
        }

        int left = 0;
        int right = 1;
        int max_profit = 0;

        while (right < prices.size()){
            if (prices[right] > prices[left]) {
                int profit = prices[right] - prices[left];
                max_profit = max(max_profit, profit);
            } else {
                left = right;
            }
            right += 1;
        }
        return max_profit;

        
    }
};
