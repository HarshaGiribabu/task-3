def is_happy_number(n):
    seen = set()
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True
def count_happy_numbers(numbers):
    count = 0
    for num in numbers:
        if is_happy_number(num):
            count += 1
    return count
numbers_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = count_happy_numbers(numbers_list)
print("Total Happy numbers in the list:", happy_count)
