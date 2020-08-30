def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
print('prime' if is_prime(n) else 'not prime')
