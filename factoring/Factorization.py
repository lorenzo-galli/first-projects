number = int(input("Insert a number to factor: "))

num_divisors = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43, 47, 53]
original_num = number
exp_dict = {}
factors = "1"


def factorizer(num):
    i = 0
    for prime in primes:
        while num != 1 and i < primes.__len__():
            if num % primes[i] == 0:
                num = num/primes[i]
                num_divisors.append(primes[i])
            else:
                i += 1
        exponent = num_divisors.count(prime)
        exp_dict[prime] = exponent


def is_prime():
    if num_divisors.__len__() == 0:
        print("Is prime")
        primes.append(number)
        print(primes)


factorizer(number)


for prime in exp_dict:
    if exp_dict[prime] == 0:
        pass
    else:
        factors += " * " + str(prime) 
        if exp_dict[prime] != 1:
            factors += "^" + str(exp_dict[prime])


def print_num():
    print(str(number) + " = " + str(factors))


is_prime()
print_num()
