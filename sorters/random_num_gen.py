import random
finish_number = 50

with open('random_numbers.txt', 'r+') as f:
    for _ in range(finish_number):
        n = random.randint(0, finish_number)
        f.write(str(n) + '\n')