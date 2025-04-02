import random

def generate_valid_numbers(count=5, min_val=10000, max_val=20000):

    numbers = set()
    while len(numbers) < count:
        num = random.randint(min_val, max_val)
        if num % 6 == 0: 
            numbers.add(num)
    return sorted(list(numbers))