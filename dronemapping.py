n=int(input("Enter the size of matrix: "))
matrix=[[0]*n for i in range (n)]                                                #2-D array initialisation to 0
for i in range(0,n):
    print(matrix[i])
print("\n")                                                                   #Intially all the elements are 0
mid=int((n-1)/2)
matrix[mid][mid]=1                                                                   #Assigning center postion to drone
ch="y"                                                                           #Terminating variable
print("Intial position\n")                                                       #Intial array with Drone in the center
for i in range(0,n):
    print(matrix[i])
print("\n")
i,j=mid,mid
while(ch=="y"):
    next=input("Enter the next position of drone: ")                            #Input next movement of Drone
    if(next=="left"):                                                           #Code if Drone moves LEFT
        if(j>0):
            matrix[i][j-1]=1
            matrix[i][j]=0
            j=j-1
        else:
            print("Lane Ends. Move in Other direction.")
    elif(next=="right"):                                                        #Code if Drone moves RIGHT
        if(j<n-1):
            matrix[i][j]=0
            j=j+1
            matrix[i][j]=1
        else:
            print("Lane Ends. Move in Other direction.")
    elif(next=="ahead"):                                                        #Code if Drone moves FORWARD
        if(i>0):
            matrix[i-1][j]=1
            matrix[i][j]=0
            i=i-1
        else:
            print("Lane Ends. Move in Other direction.")
    elif(next=="behind"):                                                       #Code if Drone moves BACKWARDS
        if(i<n-1):
            matrix[i][j]=0
            i=i+1
            matrix[i][j]=1
        else:
            print("Lane Ends. Move in Other direction.")
    else:                                                                       #Code for getting back to ORIGINAL position
        print("Returning to Original Position:")
        matrix[i][j]=0
        i,j=mid,mid
        matrix[i][j]=1
    print("Next position\n")                                                     #Printing array as the changes in position in Drone
    for r in range(0,n):
        print(matrix[r])
    print("\n")
    ch=input("Do you want to continne(y/n)")
