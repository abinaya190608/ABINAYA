def is_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Generate prime numbers between 1 and 100
prime_numbers = generate_primes(100)
print("Prime numbers between 1 and 100:", prime_numbers)
