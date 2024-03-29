def segregate_0s_and_1s(nums):

  # Two pointer approach
  left = 0
  right = len(nums) - 1

  while left < right:
    # Find the first 1 from the left side
    while left < right and nums[left] == 0:
      left += 1

    # Find the last 0 from the right side
    while left < right and nums[right] == 1:
      right -= 1

    # Swap if left and right haven't crossed
    if left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1

  return nums

def get_binary_list():
  """
  Prompts the user for comma-separated integers (0s and 1s) and validates input.
  """
  while True:
    num_str = input("Enter comma-separated integers (0s and 1s) for the list: ")
    try:
      nums = [int(num) for num in num_str.split(",")]
      # Validate if all elements are 0 or 1
      if all(num in (0, 1) for num in nums):
        return nums
      else:
        print("Invalid input: Please enter only 0s and 1s.")
    except ValueError:
      print("Invalid input: Please enter comma-separated integers.")

# Get user input and validate
nums = get_binary_list()

# Segregate 0s and 1s
sorted_list = segregate_0s_and_1s(nums)

print("Segregated list:", sorted_list)
