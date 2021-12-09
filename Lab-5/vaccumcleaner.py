def clean(floor):
    i=0
    j=0
    x=0
    perf=0
    row=len(floor)
    column=len(floor[0])
    print("Initial State is : ")
    print(floor)
 
    while(row != 0):
        if floor[i][j] == 1:
            floor[i][j]=0
            x=x+1
            print_floor(floor,i,j,x)
            j=j+1
            perf=perf+1
            print("Cleaned the Space")
            perf = perf + 1
        else:
            print("Moving Right")
            perf = perf + 1
            j=j+1
        if j==column:
            print("Moving Down")
            perf = perf + 1
            j=0
            i=i+1
            row=row-1
    performance(perf)
 
def print_floor(floor, row, col,count):# row, col represent the current vacuum cleaner position
    print('step:',count)
    for x in floor:
        print(x)
    print('vaccum cleaner :',row,col)
 
def performance(perf):
    print('The Total Step Count =')
    print(perf)
 
# Test 1
floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]
 
clean(floor)
 
# Test 2
# floor = [[1, 1, 0, 0, 1, 0, 0],
#          [0, 0, 0, 1, 0, 0, 0],
#          [0, 1, 1, 1, 1, 1, 1],
#          [0, 1, 0, 1, 0, 1, 0]]
#
# clean(floor)
