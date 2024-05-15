def find_minimum_elements(sorted_list):
    if not sorted_list:
        return None
    else:
        return sorted_list[0]  
sorted_list = [1, 2, 3, 4, 5]
minimum_element = find_minimum_elements(sorted_list)
if minimum_element is not None:
    print("The minimum element is:", minimum_element)
else:
    print("The list is empty.")
