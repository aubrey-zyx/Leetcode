/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void dfs(TreeNode node, List<Integer> path, int remainingSum, List<List<Integer>> res) {
        if (node == null) {
            return;
        }

        path.add(node.val);

        if (node.left == null && node.right == null && remainingSum == node.val) {
            res.add(new ArrayList<>(path));
        } else {
            this.dfs(node.left, path, remainingSum - node.val, res);
            this.dfs(node.right, path, remainingSum - node.val, res);
        }

        path.remove(path.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        this.dfs(root, path, targetSum, res);
        return res;
    }
}