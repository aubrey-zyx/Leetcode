class Solution {
    protected void backtrack(
        int remain,
        LinkedList<Integer> comb,
        int i,
        int[] candidates,
        List<List<Integer>> res
    ) {
        if (remain == 0) {
            res.add(new ArrayList<Integer>(comb));
            return;
        } else if (i >= candidates.length || remain < 0) {
            return;
        }

        comb.add(candidates[i]);
        backtrack(remain - candidates[i], comb, i, candidates, res);

        comb.removeLast();
        backtrack(remain, comb, i + 1, candidates, res);
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        LinkedList<Integer> comb = new LinkedList<Integer>();
        backtrack(target, comb, 0, candidates, res);
        return res;
    }
}