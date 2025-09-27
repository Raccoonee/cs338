import math

e_bob = 17
n_bob = 266473

ciphertext = [42750, 225049, 67011, 9062, 263924, 83744, 10951, 156009,
174373, 125655, 207173, 200947, 227576, 183598, 148747, 211083,
225049, 218587, 191754, 164498, 225049, 171200, 193625, 99766,
94020, 223044, 38895, 74666, 48846, 219950, 139957, 77545,
171672, 165278, 150326, 262673, 164498, 142355, 77545, 171672,
255299, 5768, 264753, 75667, 261607, 31371, 164498, 140654,
244325, 140696, 40948, 179472, 168428, 34824, 32543, 30633,
104926, 190298, 148747, 132510, 42607, 232272, 42721, 188452,
239228, 50536, 216512, 139240, 78779, 166647, 100152, 261607,
121165]

p_bob = 439
q_bob = 607

lambda_n_bob = 44238

print(f"lamda_n_bob: {math.lcm(p_bob-1, q_bob-1)}")


# helper function to check for primality
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Factor n_bob to find p and q
for p in range(2, int(n_bob ** 0.5) + 1):
    if n_bob % p == 0:
        q = n_bob // p
        if is_prime(p) and is_prime(q):
            print(f"Found primes: p = {p}, q = {q}")
            break


for d in range(1, lambda_n_bob):
    if (d * e_bob) % lambda_n_bob == 1:
        print(f"Found d: {d}")
        break

d_bob = 10409

# Decrypt each value using RSA decryption: plaintext = ciphertext^d mod n
decrypted_values = [pow(c, d_bob, n_bob) for c in ciphertext]

# Convert 2-byte blocks to ASCII characters
message = ''
for val in decrypted_values:
    # Split into high byte and low byte
    high_byte = val // 256
    low_byte = val % 256
    
    # Convert to characters
    message += chr(high_byte) + chr(low_byte)

print("Decrypted message:", message)