number = int(input("Insert a number to factor: "))

num_divisors = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43, 47, 53]
original_num = number

def factorizer(num):
    i = 0
    for prime in primes:
        while num != 1:
            if num % primes[i] == 0:
                num = num/primes[i]
                num_divisors.append(primes[i])
            i += 1
    print(num_divisors)

factorizer(number)

def is_prime(num):
   pass

for prime in primes:
    pass

def write_num(num):
    pass
