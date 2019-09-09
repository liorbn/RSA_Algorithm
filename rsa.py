from random import randrange, getrandbits, randint
level = 256

def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inv(e, phi_num):
    g, x, y = egcd(e, phi_num)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi_num


def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=2048):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        # print(counter)
        p = generate_prime_candidate(length)
    return p


def phi(prime1, prime2):
    return (prime1 - 1) * (prime2 - 1)


def generate_public_key_n(prime1, prime2):
    return prime1 * prime2


def generate_public_key_e(phi_n):
    e = 3
    while gcd(e, phi_n) != 1:
        e += 1

    return e


### Until here is rsa algorithm
p1 = generate_prime_number(level)
p2 = generate_prime_number(level)
n = generate_public_key_n(p1, p2)
phi_of_n = phi(p1, p2)
e = generate_public_key_e(phi_of_n)
d = mod_inv(e, phi_of_n)


def encrypt(message, n, e):
    if message >= n:
        print("The message must be smaller then public key n")
        return None
    cipher = pow(message, e, n)
    return cipher


def decrypt(c):
    msg = pow(c, d, n)
    return msg


def get_public_keys():
    return n, e


def set_encryption_level(new_level):
    global level
    level = new_level


