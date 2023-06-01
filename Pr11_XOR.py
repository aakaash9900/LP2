string = "Hello World"
str1 = ""
str2 = ""

for char in string:
    and_result = ord(char) & 127
    str1 += chr(and_result)

    xor_result = ord(char) ^ 127
    str2 += chr(xor_result)

print(str1)
print(str2)
