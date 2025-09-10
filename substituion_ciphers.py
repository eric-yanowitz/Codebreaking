import cipher_tests as ct
import string

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

