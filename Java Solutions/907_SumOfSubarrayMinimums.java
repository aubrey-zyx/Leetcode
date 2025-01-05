class Solution {
    public int sumSubarrayMins(int[] arr) {
        long res = 0;
        Stack<Integer> stack = new Stack<>();
        int MOD = 1000000007;

        for (int i = 0; i <= arr.length; i++) {
            while (!stack.empty() && (i == arr.length || arr[stack.peek()] >= arr[i])) {
                int mid = stack.pop();
                int left = stack.empty() ? -1 : stack.peek();
                int right = i;
                long count = (mid - left) * (right - mid);
                res += arr[mid] * count;
            }
            stack.push(i);
        }
        
        return (int) (res % MOD);
    }
}