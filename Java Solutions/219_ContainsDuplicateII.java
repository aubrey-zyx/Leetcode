class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (pos.containsKey(nums[i]) && i - pos.get(nums[i]) <= k) {
                return true;
            }
            pos.put(nums[i], i);
        }
        return false;
    }
}


class Solution2 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> seen = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.contains(nums[i])) return true;
            seen.add(nums[i]);
            if (seen.size() > k) {
                seen.remove(nums[i - k]);
            }
        }
        return false;
    }
}