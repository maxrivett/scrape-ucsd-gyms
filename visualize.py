file1 = open("txtfiles/alt.txt","r")

def compile() :
    rows, cols = (0, 4)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    cnt = 0
    for line in file1 :
        line = line[:-1]
        if cnt%4 == 0:
            innerArr = [line, 0, 0, 0]
            arr.append(innerArr)
        else :
            arr[cnt//4][cnt%4] = line
        cnt = cnt + 1
    
    return arr

a = compile()
print(a)
file1.close()