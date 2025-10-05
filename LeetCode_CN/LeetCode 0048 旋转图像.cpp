class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size_n = matrix.size();
        int matrix_x = floor(double(size_n) / 2), matrix_y = ceil(double(size_n) / 2);
        for(int i = 0; i < matrix_x; i++){
            for(int j = 0; j < matrix_y; j++){
                int mem_num = matrix[i][j], x = i, y = j;
                for(int k = 0;k < 4; k++){
                    swap(x,y);
                    y = abs(y - size_n + 1);
                    swap(mem_num, matrix[x][y]);
                }
            }
        }
    }
};