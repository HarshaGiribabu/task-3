def sub_list_with_sum_zero(nums):
    prefix_sum = 0
    sum_set = set()
    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in sum_set:
            return True
        sum_set.add(prefix_sum)
    return False
nums = [4, 2, -3, 1, 6]
if sub_list_with_sum_zero(nums):
    print(" a sublist with sum equal to zero.")
else:
    print(" no sublist with sum equal to zero.")
