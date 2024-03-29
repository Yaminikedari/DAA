def find_inversion_count_and_pairs(nums):
  """
  Finds the total number of inversions (i, j) in a list `nums` such that i < j and nums[i] > nums[j].
  Also prints the inversion pairs.

  Args:
      nums: A list of integers.

  Returns:
      A tuple containing the total number of inversions and a list of inversion pairs.
  """

  def merge_and_count(left, right):
    """
    Merges two sorted sub-arrays and counts inversions during merging, recording pairs.

    Args:
        left: A sorted sub-array (list).
        right: A sorted sub-array (list).

    Returns:
        A tuple containing the merged sorted sub-array, the inversion count, and a list of inversion pairs.
    """
    i, j, count = 0, 0, 0
    merged = []
    inversion_pairs = []

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        merged.append(left[i])
        i += 1
      else:
        # Count inversions and record pairs
        count += len(left) - i
        for k in range(i, len(left)):
          inversion_pairs.append((left[k], right[j]))
        merged.append(right[j])
        j += 1

    # Append remaining elements (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count, inversion_pairs

  # Divide and Conquer approach using merge sort
  def merge_sort_and_count(nums):
    if len(nums) <= 1:
      return nums, 0, []

    mid = len(nums) // 2
    left, left_count, left_pairs = merge_sort_and_count(nums[:mid])
    right, right_count, right_pairs = merge_sort_and_count(nums[mid:])

    merged, merge_count, merge_pairs = merge_and_count(left, right)
    return merged, left_count + right_count + merge_count, left_pairs + right_pairs + merge_pairs

  # Sort and count inversions
  sorted_nums, inversion_count, inversion_pairs = merge_sort_and_count(nums)
  return inversion_count, inversion_pairs

# Get user input for the list of integers
num_str = input("Enter comma-separated integers for the list: ")
nums = [int(num) for num in num_str.split(",")]

inversion_count, inversion_pairs = find_inversion_count_and_pairs(nums)
print("Inversion count:", inversion_count)

if inversion_pairs:
  print("Inversion pairs:", inversion_pairs)
else:
  print("No inversion pairs found.")
