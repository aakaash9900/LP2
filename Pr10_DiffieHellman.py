def generate_key(p, g, a, b):
    # Public key calculation
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Secret key calculation
    secret_key_A = pow(B, a, p)
    secret_key_B = pow(A, b, p)

    # Return the public keys and secret keys
    return A, B, secret_key_A, secret_key_B

def main():
    # Prompt the user for the modulo (prime number), primitive root, and private keys
    p = int(input("Enter the value of modulo (prime number): "))
    g = int(input("Enter the primitive root: "))
    a = int(input("Enter the private key of Alice: "))
    b = int(input("Enter the private key of Bob: "))

    # Generate the public keys and secret keys
    A, B, secret_key_A, secret_key_B = generate_key(p, g, a, b)

    # Print the public keys and secret keys
    print("Public key of Alice (A):", A)
    print("Public key of Bob (B):", B)
    print("Secret key of Alice:", secret_key_A)
    print("Secret key of Bob:", secret_key_B)

    # Check if the secret keys match
    if secret_key_A == secret_key_B:
        print("Alice and Bob can communicate.")
        print("They share the same secret key:", secret_key_A)
    else:
        print("Alice and Bob cannot communicate.")
        print("Their secret keys are not the same.")

if __name__ == "__main__":
    main()