def find_triplet(nums, target):

  nums.sort()

  for i in range(len(nums) - 2):
    left, right = i + 1, len(nums) - 1
    while left < right:
      current_sum = nums[i] + nums[left] + nums[right]
      if current_sum == target:
        return [nums[i], nums[left], nums[right]]
      elif current_sum < target:
        left += 1
      else:
        right -= 1
  return []
nums = [10, 20, 30, 9]
target = 59
triplet = find_triplet(nums, target)

if triplet:
  print(f"Triplet found: {triplet}")
else:
  print(f"No triplet found that sums to {target}")
