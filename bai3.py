def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, left, right):
    if left < right:
    #Nếu kích thước nhỏ hơn 10 thì dùng insertion sort
        if right - left < 10:
            insertion_sort(arr, left, right)
        else:
            mid = (left + right) // 2
            pivot = arr[mid]
            arr[mid], arr[right] = arr[right], arr[mid]
            i = left - 1
            for j in range(left, right):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            quicksort(arr, left, i)
            quicksort(arr, i + 2, right)

def hybrid_sort(arr):
    quicksort(arr, 0, len(arr) - 1)

arr = [3, 2, 1, 5, 4, 7, 6]
hybrid_sort(arr)
print(arr)
