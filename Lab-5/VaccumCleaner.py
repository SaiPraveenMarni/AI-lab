def clean(floor):
    i=0
    j=0
    x=0
    row=len(floor)
    column=len(floor[0])
    while(row != 0):
        if floor[i][j] == 1:
            floor[i][j]=0
            x=x+1
            print_floor(floor,i,j,x)
            j=j+1
        else:
            j=j+1
        if j==column:
            j=0
            i=i+1
            row=row-1

def print_floor(floor, row, col,count):# row, col represent the current vacuum cleaner position
    print('step:',count)
    for x in floor:
        print(x)
    print('vaccum cleaner :',row,col)

# Test 1
floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]

clean(floor)

# Test 2
floor = [[1, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0, 1, 0]]

clean(floor)


---------------------------------------------------------------------------------------------------------------------------------------------------------------
****************************************************************************************************************************************************************
----------------------------------------------------------------------------------------------------------------------------------------------------------------


C:\Users\ravis\PycharmProjects\exercises\venv\Scripts\python.exe C:/Users/ravis/PycharmProjects/exercises/lab5.py
step: 1
[0, 0, 0, 0]
[0, 1, 0, 1]
[1, 0, 1, 1]
vaccum cleaner : 0 0
step: 2
[0, 0, 0, 0]
[0, 0, 0, 1]
[1, 0, 1, 1]
vaccum cleaner : 1 1
step: 3
[0, 0, 0, 0]
[0, 0, 0, 0]
[1, 0, 1, 1]
vaccum cleaner : 1 3
step: 4
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 1, 1]
vaccum cleaner : 2 0
step: 5
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 1]
vaccum cleaner : 2 2
step: 6
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
vaccum cleaner : 2 3

Process finished with exit code 0

---------------------------------------------------------------------------------------------------------------------------------------------------------------
****************************************************************************************************************************************************************

C:\Users\ravis\PycharmProjects\exercises\venv\Scripts\python.exe C:/Users/ravis/PycharmProjects/exercises/lab5.py
step: 1
[0, 1, 0, 0, 1, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 0 0
step: 2
[0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 0 1
step: 3
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 0 4
step: 4
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 1 3
step: 5
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 1
step: 6
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 2
step: 7
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 3
step: 8
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 4
step: 9
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 5
step: 10
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 0, 1, 0]
vaccum cleaner : 2 6
step: 11
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 1, 0]
vaccum cleaner : 3 1
step: 12
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0]
vaccum cleaner : 3 3
step: 13
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
vaccum cleaner : 3 5

Process finished with exit code 0