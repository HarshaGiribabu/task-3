def first_non_repeating_element(nums):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) +1
    for num in nums:
        if freq_dict[num] == 1:
            return num
    return None
nums = [1, 2, 3, 4, 2, 3, 1, 5, 6, 5, 6]
result = first_non_repeating_element(nums)
if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found.")
