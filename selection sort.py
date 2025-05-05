def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test
arr = [29, 10, 14, 37, 13]
print("Sorted Array:", selection_sort(arr))
# Get user input
# user_input = input("Enter numbers separated by spaces: ")
# arr = list(map(int, user_input.split()))

# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)