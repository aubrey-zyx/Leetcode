class Solution {
    private char[][] board;
    private int ROWS;
    private int COLS;
    private String word;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.ROWS = board.length;
        this.COLS = board[0].length;
        this.word = word;

        for (int r = 0; r < this.ROWS; r++) {
            for (int c = 0; c < this.COLS; c++) {
                if (this.dfs(r, c, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(int r, int c, int i) {
        if (i == this.word.length()) return true;

        if (
            r < 0 || r >= this.ROWS ||
            c < 0 || c >= this.COLS ||
            this.board[r][c] != word.charAt(i)
        ) return false;

        this.board[r][c] = '#';
        boolean res = false;

        int[] rDirections = {0, 1, 0, -1};
        int[] cDirections = {1, 0, -1, 0};
        for (int d = 0; d < 4; d++) {
            res = this.dfs(r + rDirections[d], c + cDirections[d], i + 1);
            if (res) break;
        }

        this.board[r][c] = word.charAt(i);
        return res;
    }
}