class NumMatrix {
    int[][] prefsum;

    public NumMatrix(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        prefsum = new int[rows + 1][cols + 1];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                prefsum[r + 1][c + 1] = prefsum[r][c + 1] + prefsum[r + 1][c] - prefsum[r][c] + matrix[r][c];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefsum[row2 + 1][col2 + 1] - prefsum[row1][col2 + 1] - prefsum[row2 + 1][col1] + prefsum[row1][col1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */