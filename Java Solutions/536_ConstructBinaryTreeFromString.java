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
    public TreeNode str2tree(String s) {
        if (s.isEmpty()) {
            return null;
        }

        StringBuilder num = new StringBuilder();
        Stack<TreeNode> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c) || c == '-') {
                num.append(c);
            } else if (c == '(') {
                if (!num.isEmpty()) {
                    TreeNode node = new TreeNode(Integer.parseInt(num.toString()));
                    num.setLength(0);
                    stack.push(node);
                }
            } else if (c == ')') {
                TreeNode node;
                if (!num.isEmpty()) {
                    node = new TreeNode(Integer.parseInt(num.toString()));
                } else {
                    node = stack.pop();
                }
                num.setLength(0);
                if (stack.peek().left == null) {
                    stack.peek().left = node;
                } else {
                    stack.peek().right = node;
                }
            }
        }

        return stack.empty() ? new TreeNode(Integer.parseInt(num.toString())) : stack.peek();
    }
}