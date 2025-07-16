alphabet = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8], 
[4, 0, 4, 2, 8], 
[2, 4, 0, 4, 8], 
[4, 2, 4, 0, 8], 
[8, 8, 8, 8, 8]]

def globalAlignment(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0]* (len(y) + 1))
    
    # fill first column (vertical direction = gap in y)
    for i in range(1, len(x) + 1):
        # char = x[i -1] , char = 'T', 'A',
        # alphabet.index(x[i - 1]), 3, 0,
        # score[alphabet.index(x[i - 1])][-1], 8, 8
        D[i][0] = D[i - 1][0] + score[alphabet.index(x[i - 1])][-1]

    # fill first row (horizontal direction = gap in x)
    for i in range(1, len(y) + 1):
        # char = y[i -1] , char = 'T', 'A',
        # alphabet.index(y[i - 1]), 3, 0,
        # score[-1][alphabet.index(y[i - 1])], 8, 8
        D[0][i] = D[0][i - 1] + score[-1][alphabet.index(y[i - 1])]

    #Loop through rest of table (i = row, j = column), comparing x[i-1] to y[j-1].    
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j - 1] + score[-1][alphabet.index(y[j -1])]
            #distHor = 16

            distVer = D[i - 1][j] + score[alphabet.index(x[i - 1])][-1]
            #distVer = 16
        
            if x[i -1] == y[j - 1]:
                distDiag = D[i - 1][j - 1]
            else:
                distDiag = D[i - 1][j - 1] + score[alphabet.index(x[i -1])][alphabet.index(y[j-1])]
            D[i][j] = min(distHor, distVer, distDiag)
    print(D)
    return D[-1][-1]

x = 'TACC'
y = 'CACC'
print(globalAlignment(x, y))