class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put('(', ')');
        pairs.put('[', ']');
        pairs.put('{', '}');

        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty() || ch != pairs.get(stack.peek())) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}