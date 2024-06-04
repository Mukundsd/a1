n=8
def solve(board,col):
    if col==n:
        print (board)
        return True
    for i in range(n):
        if issafe(board,i,col):
            board[i][col]=1
            if solve(board,col+1):
                return True
            board[i][col]=0
    return False
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    for x,y in zip(range(row,n,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    return True
board=[[0 for i in range (n)]for j in range (n)]
if not solve(board,0):
    print("not have sol")
        

