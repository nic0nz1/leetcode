class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        for i in range(3, numRows + 1):
            row = [1]
            for j in range(i-2):
                row.append(res[-1][j] + res[-1][j+1])
            row.append(1)
            res.append(row)
        return res