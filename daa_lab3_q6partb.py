def two_sum_n_log_n(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True, arr[left], arr[right]
        elif current_sum < K:
            left += 1
        else:
            right -= 1
            
    return False, None, None

# Example usage:
arr = [8, 4, 1, 6]
K = 10
exists, num1, num2 = two_sum_n_log_n(arr, K)
if exists:
    print(f"Yes, {num1} and {num2} sum up to {K}.")
else:
    print("No such pair exists.")
