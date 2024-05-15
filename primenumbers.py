
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = []
prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
        prime_count += 1
print("Number of prime numbers:", prime_count)
print("Prime numbers:", prime_numbers)
