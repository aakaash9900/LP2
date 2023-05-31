import math

def gcd(e, z):
    if e == 0:
        return z
    else:
        return (z % e, z)

p = int(input("Enter 1st prime number :"))
q = int(input("Enter 2nd prime number :"))
z = (p - 1) * (q - 1)
n = p * q

print("The value of z :", z)
e = 2
while e < z and gcd(e, z) == 1:
    break
e += 1

print("The value of e :", e)

d = 0
for i in range(10):
    x = 1 + (z * i)
    if x % e == 0:
        d = x // e
        break

print("The value of d : ", d)

msg = int(input("Enter the number of message to be encrypted and decrypted :"))
c = (msg ** e) % n

C = c
N = n

msgback = (C ** d) % N

print("Encrypted message is :", c)
print("Decrypted message is :", msgback)