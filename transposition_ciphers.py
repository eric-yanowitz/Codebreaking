#decipher a caesar cipher with a key (key pushes the original alphabet forward i.e. pushes the replacement alphabet backwards)
#option for abbreviated decipher (first 25 characters) and partial decipher (i.e. letters between '^' aren't deciphered)
def caesar_cipher(ciphertext, key = 0, abbreviated = False, partial = False):
    plaintext = ""
    if key > 25 or key < 0:
        plaintext = "key must be 0 through 25"
        return plaintext
    skip_count = 0
    for i in range(len(ciphertext)):
        if abbreviated == True and i == 24:
            break
        j = ciphertext[i]
        if skip_count != 0 and partial == True:
            skip_count -= 1
            continue
        if partial == True and j == "^":
            count = i + 1
            while ciphertext[count] != "^":
                plaintext += ciphertext[count]
                count += 1
                skip_count += 1
            skip_count += 1
            continue

        if j.isalpha():
            j = j.lower()
            n = ord(j) - key
            if n >= 97:
                plaintext += chr(n)
            else:
                plaintext += chr(n + 26)   
        else:
            plaintext += j
    return plaintext

# caesar cipher exhaustive; all 25 codes
def caesar_cipher_ex(ciphertext, abbreviated = False, partial = False):
    plaintext = ""
    for i in range(0, 26):
        plaintext += f"key = {i}: "
        plaintext += caesar_cipher(ciphertext, i, abbreviated, partial)
        plaintext += "\n\n"
    return plaintext