def partition_mid(arr):
    mid = (len(arr) - 1) // 2
    pivot = arr[mid]
    left = []
    right = []
    #Duyệt qua từng phần tử trong mảng. Nếu phần tử không phải là pivot, 
    #kiểm tra nếu nhỏ hơn hoặc bằng pivot thì thêm vào mảng left, ngược lại thêm vào mảng right.
    for i in range(len(arr)):
        if i != mid:
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
    
    # Nối mảng left, pivot và right lại với nhau
    arr = left + [pivot] + right
    # Tìm index mới của pivot sau khi đã chuyển các phần tử
    new_pivot_index = len(left)
    
    return arr, new_pivot_index

arr = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
arr_partitioned, pivot_index = partition_mid(arr)
print(arr_partitioned)
print(pivot_index)
