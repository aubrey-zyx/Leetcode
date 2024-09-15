class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0, prefSum = 0;
        HashMap<Integer, Integer> mp = new HashMap<>();
        mp.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            prefSum += nums[i];
            res += mp.getOrDefault(prefSum - k, 0);
            mp.put(prefSum, mp.getOrDefault(prefSum, 0) + 1);
        }
        return res;
    }
}