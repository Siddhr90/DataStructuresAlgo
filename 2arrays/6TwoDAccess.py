

print(twoDarray)

def accessEle(twoDarray, row_idx, col_idx):
    if row_idx >= len(twoDarray) or col_idx >= len(twoDarray[0]):
        print('incorrect index')
    else:
        print(twoDarray[row_idx][col_idx])


accessEle(twoDarray,1,3)

print(twoDarray[:][1])

def traverse2D(twoDarray):
    for i in range(len(twoDarray)):
        for j in range(len(twoDarray[0])):
            print(twoDarray[i][j])

#traverse2D(twoDarray) O(mn)





