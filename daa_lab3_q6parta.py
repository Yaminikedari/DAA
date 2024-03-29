def two_sum_n_squared(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == K:
                return True, arr[i], arr[j]
    return False, None, None

# Example usage:
arr = [8, 4, 1, 6]
K = 10
exists, num1, num2 = two_sum_n_squared(arr, K)
if exists:
    print(f"Yes, {num1} and {num2} sum up to {K}.")
else:
    print("No such pair exists.")
