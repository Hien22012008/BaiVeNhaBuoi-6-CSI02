def quicksort(arr):
    #Kiểm tra nếu mảng có độ dài nhỏ hơn hoặc bằng 1, tức là không cần sắp xếp, trả về mảng như hiện tại.
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        #Sử dụng list comprehension để tạo mảng left chứa các phần tử nhỏ hơn hoặc bằng pivot.
        left = [x for x in arr[:mid] + arr[mid + 1:] if x <= pivot]
        #Sử dụng list comprehension để tạo mảng right chứa các phần tử lớn hơn pivot.
        right = [x for x in arr[:mid] + arr[mid + 1:] if x > pivot]
        #Kiểm tra nếu mảng có độ dài nhỏ hơn hoặc bằng 1, tức là không cần sắp xếp, trả về mảng như hiện tại.
        return quicksort(left) + [pivot] + quicksort(right)
    
arr = [7, 6, 5, 4, 3, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)