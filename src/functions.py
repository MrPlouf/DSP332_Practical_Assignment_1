import random

#function to create the  random numbers to start the game with in a list (set usage)
def generate_valid_numbers(count=5):

    numbers = set()
    while len(numbers) < count:

        num= random.randint(10000, 20000)
        if num % 6 == 0: 
            numbers.add(num)
            
    return list(numbers)