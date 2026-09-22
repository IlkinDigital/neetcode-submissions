class Solution:
    def init_set(self, length):
        res = []
        for _ in range(length):
            res.append(set())

        return res
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = self.init_set(len(board))
        cols = self.init_set(len(board))
        sqrs = self.init_set(len(board))

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                num = int(num)
                sqr = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in sqrs[sqr]:
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    sqrs[sqr].add(num)

        return True
                    