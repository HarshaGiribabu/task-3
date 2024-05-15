def find_duplicates(list1, list2, list3):
    combined_list = list1 + list2 + list3
    count_dict = {}
    duplicates = []
    for item in combined_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    for item, count in count_dict.items():
        if count > 1:
            duplicates.append(item)
    return duplicates
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [6, 7, 8, 9, 10]
duplicates = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", duplicates)
