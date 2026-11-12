class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rep = {}
        for i in range(1, 10):
            rep[i] = []
        for i in range(len(board)):
            occ = []
            for j in range(len(board[i])):        
                if board[i][j] != "." and board[i][j] in occ:
                    return False
                elif board[i][j] != ".":
                    occ.append(board[i][j])
        for i in range(len(board)):
            occ = []
            for j in range(len(board[i])):  
                if board[j][i] != "." and board[j][i] in occ:
                    return False
                elif board[j][i] != ".":
                    occ.append(board[j][i])
        for i in range(len(board)):
            for j in range(len(board[i])):        
                if i >= 0 and i < 3 and j < 3 and j >= 0:
                    if board[i][j] != "." and board[i][j] in rep[1]:
                        return False
                    elif board[i][j] != ".":
                        rep[1].append(board[i][j])
                if i >= 0 and i < 3 and j < 6 and j >= 3:
                    if board[i][j] != "." and board[i][j] in rep[2]:
                        return False
                    elif board[i][j] != ".":
                        rep[2].append(board[i][j])
                if i >= 0 and i < 3 and j < 9 and j >= 6:
                    if board[i][j] != "." and board[i][j] in rep[3]:
                        return False
                    elif board[i][j] != ".":
                        rep[3].append(board[i][j])
                if i >= 3 and i < 6 and j < 3 and j >= 0:
                    if board[i][j] != "." and board[i][j] in rep[4]:
                        return False
                    elif board[i][j] != ".":
                        rep[4].append(board[i][j])
                if i >= 3 and i < 6 and j < 6 and j >= 3:
                    if board[i][j] != "." and board[i][j] in rep[5]:
                        return False
                    elif board[i][j] != ".":
                        rep[5].append(board[i][j])
                if i >= 3 and i < 6 and j < 9 and j >= 6:
                    if board[i][j] != "." and board[i][j] in rep[6]:
                        return False
                    elif board[i][j] != ".":
                        rep[6].append(board[i][j])
                if i >= 6 and i < 9 and j < 3 and j >= 0:
                    if board[i][j] != "." and board[i][j] in rep[7]:
                        return False
                    elif board[i][j] != ".":
                        rep[7].append(board[i][j])
                if i >= 6 and i < 9 and j < 6 and j >= 3:
                    if board[i][j] != "." and board[i][j] in rep[8]:
                        return False
                    elif board[i][j] != ".":
                        rep[8].append(board[i][j])
                if i >= 6 and i < 9 and j < 9 and j >= 6:
                    if board[i][j] != "." and board[i][j] in  rep[9]:
                        return False
                    elif board[i][j] != ".":
                        rep[9].append(board[i][j])
        return True
               