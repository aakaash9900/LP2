def decrypt_transposition(ciphertext, key):
    num_rows = len(ciphertext) // key                                 # Calculate the number of rows required
    if len(ciphertext) % key != 0:
        num_rows += 1
    num_columns = key                                                  # Calculate the number of columns

    matrix = [[''] * num_columns for _ in range(num_rows)]             # Create the matrix for decryption

    index = 0                                                           # Populate the matrix with the ciphertext
    for col in range(num_columns):
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1

    plaintext = ''                                                    # Read the decrypted message row by row
    for row in range(num_rows):
        for col in range(num_columns):
            plaintext += matrix[row][col]
    return plaintext

ciphertext = "Tasoaygdnio"
key = 3

plaintext = decrypt_transposition(ciphertext, key)
print("Ciphertext:",ciphertext)
print("Plaintext:",plaintext)