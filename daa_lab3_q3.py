def find_swapped_elements(arr):
    first_wrong = None
    second_wrong = None
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first_wrong is None:
                first_wrong = i
            else:
                second_wrong = i + 1
                break
    
    return first_wrong, second_wrong

def sort_array_with_swapped_elements(arr):
    first_wrong, second_wrong = find_swapped_elements(arr)
    
    arr[first_wrong], arr[second_wrong] = arr[second_wrong], arr[first_wrong]
    
    return sorted(arr)

# Take input from the user
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

sorted_arr = sort_array_with_swapped_elements(arr)
print("Sorted array with swapped elements:", sorted_arr)
