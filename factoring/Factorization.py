# A factorizator developed by Lorenzo Galli 

print('Enter a number and this project will factorize it for you.')
print('Numbers that have factors larger than 7919 (999th prime) won\'t be factorized')
number = int(input("Insert a number to factor: "))

# Declare variables and initialize lists and dictionaries
num_divisors = []
original_num = number
exp_dict = {}
factors = "1"

# Open the file with the primes, reads it and creates a list 
with open('primes.txt', 'r') as f:
    primes =[]
    for line in f:
        line = line.strip()
        line = int(line)
        primes.append(line)

# This is the main function, it takes as input the user number
def factorizer(num):
    # Add a index to select the prime
    i = 0    
    for prime in primes:
        # If num = 1 it means we succesfully factorized it also i cannot
        # be bigger than the lenght of the list or it will throw an error
        while num != 1 and i < primes.__len__():
            # If the number is divisible it adds it to the divisors list
            if num % primes[i] == 0:
                num = num/primes[i]
                num_divisors.append(primes[i])
            # If not it just changes prime and repeat the cicle
            else:
                i += 1
        # Some primes might be repeated so we use exponents
        exponent = num_divisors.count(prime)
        exp_dict[prime] = exponent


# This function prints if the number is prime and its factors 
def print_num():
    if num_divisors.__len__() == 1:
        print("Is prime")
    else:
        print("It's not prime")
    print(str(number) + " = " + str(factors))


factorizer(number)

# This loop creates the final string with the factors
for prime in exp_dict:
    # If it isn't a factor it doesn't display it
    if exp_dict[prime] == 0:
        pass
    # If it is it displays a * with the factors
    else:
        factors += " * " + str(prime) 
        # If it has an exp it displays it with ^
        if exp_dict[prime] != 1:
            factors += "^" + str(exp_dict[prime])


print_num()
