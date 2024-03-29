def find_two_largest_and_product(nums):
  """
  Finds the two largest numbers in the given unsorted list `nums` and returns their product.

  Args:
      nums: A list of integers.

  Returns:
      A tuple containing the two largest numbers and their product, or None if the list is empty.
  """

  if not nums:  # Check if the list is empty
    return None  # Return None to indicate an empty list

  # Initialize with the first element for comparison
  largest1 = nums[0]

  for num in nums[1:]:
    # Update largest1 if the current number is larger
    if num > largest1:
      largest1 = num

  # Find the second largest number (excluding the largest)
  largest2 = max(num for num in nums if num != largest1)  # List comprehension for filtering

  return largest1, largest2, largest1 * largest2

# Get user input for the list of integers
num_str = input("Enter comma-separated integers for the list: ")
nums = [int(num) for num in num_str.split(",")]

largest1, largest2, product = find_two_largest_and_product(nums)

if largest1 is not None:  # Check if list wasn't empty
  print("Two largest numbers:", largest1, largest2)
  print("Product of the two largest numbers:", product)
else:
  print("The list is empty.")
