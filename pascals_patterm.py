n = int(input("enter no of rows : "))
list_pascal = list()
for i in range(n):
    temp_list = []
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list_pascal[i-1][j-1] + list_pascal[ i-1][j])
    list_pascal.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(list_pascal[i][j], end=" ")
    print()

# output
# enter no of rows : 5
#     1 
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1