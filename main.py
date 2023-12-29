def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


test_arr = [70, 13, 2, 56, 8, 29, 75, 45, 85]
quick_sort(test_arr)
print(quick_sort(test_arr))
