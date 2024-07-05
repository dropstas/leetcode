class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def one(board):
            seen = set()
            for i in board:
                for j in i:
                    if j != '.':
                        if j not in seen:
                            seen.add(j)
                        else:
                            return False
                seen = set()
            return True

        def two(board):
            seen = set()
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[j][i] != '.':
                            if board[j][i] not in seen:
                                seen.add(board[j][i])
                            else:
                                return False
                seen = set()
            return True

        def three(board):
            n = 0
            m = 0
            list2 = []
            for z in range(3):
                for i in range(3):
                    list = []
                    for j in (board[m:m+3]):
                        for k in (j[n:n+3]):
                            list.append(k)
                    n = n + 3
                    list2.append(list)
                n = 0
                m = m + 3

            return one(list2)
    
        return one(board) and two(board) and three(board)