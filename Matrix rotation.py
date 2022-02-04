first_multiple_input = input().rstrip().split()

rows = int(first_multiple_input[0])

colums = int(first_multiple_input[1])

a = int(first_multiple_input[2])
matrix = []
for _ in range(rows):
        matrix.append(list(map(int, input().rstrip().split())))
k=0
bufcount1=int
bufcount2=int
l=rows-1
c=0
m=colums-1
for i in range(a):
    k=0
    l=rows-1
    c=0
    m=colums-1
    if rows<colums:
        param=rows
    else:
        param=colums
    while param/2 != c:
        i=rows-1-c
        j=colums-1-c
        bufcount1=matrix[i][j]
        while i!=k+c:
            bufcount2=matrix[i-1][j]
            matrix[i-1][j]=bufcount1
            bufcount1=bufcount2
            i=i-1
        while j!=k+c:
            bufcount2=matrix[i][j-1]
            matrix[i][j-1]=bufcount1
            bufcount1=bufcount2
            j=j-1    
        while i!=l-c:
            bufcount2=matrix[i+1][j]
            matrix[i+1][j]=bufcount1
            bufcount1=bufcount2
            i=i+1
        while j!=m-c:
            bufcount2=matrix[i][j+1]
            matrix[i][j+1]=bufcount1
            bufcount1=bufcount2
            j=j+1 
        c+=1    

    
for i in range(rows):
    for j in range(colums):
        print(matrix[i][j],end=' ')
    print()    