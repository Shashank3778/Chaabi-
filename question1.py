def selectionSort( List ):
    n = len( List )
    for i in range( n - 1 ): 
        min = i

        for j in range( i + 1, n ):
            if List[j] < List[min] :
                min = j

        if min != i :
            temp = List[i]
            List[i] = List[min]
            List[min] = temp

    return List


List = [] 
n = int(input("Enter number of elements : "))
print("enter the elements")
for i in range(0, n):
     x= int(input())
     List.append(x)
sorted_list = selectionSort(List)
print(sorted_list)  
