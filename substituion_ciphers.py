import cipher_tests as ct
import string
#decipher a caesar cipher with a key (key pushes the original alphabet forward i.e. pushes the replacement alphabet backwards)
#option for abbreviated decipher (first 25 characters) and partial decipher (i.e. letters between '^' aren't deciphered)
def caesar_decipher(ciphertext, key = 0, abbreviated = False, partial = False):
    plaintext = ""
    if key > 25 or key < 0:
        plaintext = "improper key value"
        return plaintext
    skip_count = 0
    for i in range(len(ciphertext)):
        if abbreviated == True and i > 24:
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
# options for abbreviated and partial like caesar_decipher()
def caesar_decipher_ex(ciphertext, abbreviated = False, partial = False):
    plaintext = ""
    for i in range(0, 26):
        plaintext += f"key = {i}: "
        plaintext += caesar_decipher(ciphertext, i, abbreviated, partial)
        plaintext += "\n\n"
    return plaintext


#letter substitution cipher
def substitution_cipher(ciphertext, cipherkey = "", d1 = {}, **kwargs):
    plaintext = ""
    d = dict.fromkeys(string.ascii_lowercase, '')
    for key in d:
        d[key] = ord(key.upper())
    if len(cipherkey) == 26:
        cipherkey.lower()
        for i in range(97,123):
            d[chr(i)] = cipherkey[i-97]
    elif len(kwargs) > 0:
        for key, value in kwargs.items():
            key = key.lower()
            d[key] = value.lower()    
    elif len(d1) > 0:
        for key, value in d1.items():
            key = key.lower()
            d[key] = value.lower()
    else:
        return
    d_swap = {value: key for key, value in d.items()}
    for i in ciphertext:
        if i.lower() in d_swap:
            plaintext += d_swap[i.lower()]
        elif i.isalpha():
            plaintext += i.upper()
        else:
            plaintext += i
    return plaintext


cryptogram = "AzQr qR X YQKZLS aLfA hQflW OQAZ YXKqaXvR."
print(substitution_cipher(cryptogram, t='a', a='x', e='l', i='q', p='k', h ='z', w='o', x='f', m='h', s='r', r='s', d='w', c='y', l ='v'))
print(substitution_cipher(cryptogram, cipherkey = "xBywlFGzqJKvhNokQsraUVofYZ"))
d = {'t': 'a', 'a': 'x', 'e': 'l'}
print(substitution_cipher(cryptogram, d1 = d))