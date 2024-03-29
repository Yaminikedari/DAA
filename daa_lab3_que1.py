def find_all_pairs_with_sum(nums, target):
  """
  Finds all possible pairs in the given unsorted list `nums` that add up to the `target` sum.

  Args:
      nums: A list of integers.
      target: The target sum.

  Returns:
      A list containing all unique pairs that add up to the target sum.
  """

  seen = set()
  all_pairs = []

  for num in nums:
    complement = target - num
    if complement in seen:
      all_pairs.append([complement, num])
    seen.add(num)

  return all_pairs

# Get user input for the list of integers
num_str = input("Enter comma-separated integers for the list: ")
nums = [int(num) for num in num_str.split(",")]

# Get user input for the target sum
target = int(input("Enter the target sum: "))

all_pairs = find_all_pairs_with_sum(nums, target)

if all_pairs:
  print("All possible pairs that add up to", target, ":")
  for pair in all_pairs:
    print(pair)
else:
  print("No pairs found with that target sum")
