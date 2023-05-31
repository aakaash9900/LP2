def encrypt_transposition(plaintext, key):
    plaintext = plaintext.replace(" ", "")                               # Remove any spaces from the plaintext
    num_columns = len(plaintext) // key                                 # Calculate the number of rows and columns based on the key

    if len(plaintext) % key != 0:
        num_columns += 1

    matrix = [[''] * num_columns for _ in range(key)]                       # Create an empty matrix for encryption

    index = 0                                                            # Populate the matrix with the plaintext column by column
    for col in range(num_columns):
        for row in range(key):
            if index < len(plaintext):
                matrix[row][col] = plaintext[index]
                index += 1

    ciphertext = ''                                                     # Read the encrypted message column by column
    for row in range(key):
        for col in range(num_columns):
            ciphertext += matrix[row][col]
    return ciphertext

plaintext = input("Enter text:")
key = 3

ciphertext = encrypt_transposition(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

