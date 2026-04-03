class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hashmap = {}
            for j in range(len(board[i])):
                if board[i][j].isnumeric() and board[i][j] in hashmap.keys():
                    return False
                elif board[i][j].isnumeric():
                    hashmap[board[i][j]] = 1
        
        for i in range(len(board[0])):
            hashmap2 = {}
            for j in range(len(board)):
                if board[j][i].isnumeric() and board[j][i] in hashmap2.keys():
                    return False
                elif board[j][i].isnumeric():
                    hashmap2[board[j][i]] = 1
        for x in [0, 3 ,6]:
            for p in [0, 3, 6]:
                square = []
                for i in range(p,p+3):
                    for j in range(x,x+3):
                        if board[i][j].isnumeric():
                            square.append(board[i][j])
                if len(set(square)) != len(square):
                    return False
        return True

        
        
        
        
        
        


        