import cipher_tools as ct
import string

#letter substitution cipher 
# def substitution_cipher(ciphertext, cipherkey = "", d1 = {}, **kwargs):
#     plaintext = ""
#     d = dict.fromkeys(string.ascii_lowercase, '')
#     for key in d:
#         d[key] = ord(key.upper())
#     if len(cipherkey) == 26:
#         cipherkey.lower()
#         for i in range(97,123):
#             d[chr(i)] = cipherkey[i-97]
#     elif len(kwargs) > 0:
#         for key, value in kwargs.items():
#             key = key.lower()
#             d[key] = value.lower()    
#     elif len(d1) > 0:
#         for key, value in d1.items():
#             key = key.lower()
#             d[key] = value.lower()
#     else:
#         return
#     d_swap = {value: key for key, value in d.items()}
#     for i in ciphertext:
#         if i.lower() in d_swap:
#             plaintext += d_swap[i.lower()]
#         elif i.isalpha():
#             plaintext += i.upper()
#         else:
#             plaintext += i
#     return plaintext

# li = [['a', []], ['b', []], ['c', []], ['d', []], ['e', []], ['f', []], ['g', []], ['h', []], ['i', []], ['j', []], ['k', []], ['l', []], ['m', []], ['n', []], ['o', []], ['p', []], ['q', []], ['r', []], ['s', []], ['t', []], ['u', []], ['v', []], ['w', []], ['x', []], ['y', []], ['z', []]] #reverse key


#substitution cipher with the possibility of multiple letters in the ciphertext standing for the same letter in the plaintext; and input = reverse key, not encryption key
def simple_sub_cipher(ciphertext, reverse_cipherkey = "", d1 = [], **kwargs):
    plaintext = ""
    d = dict.fromkeys(string.ascii_lowercase, '') #reverse key
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            key = key.lower()
            d[key] = value.lower()
    else: 
        return
    for key in d:
        if len(d[key]) == 0:
            d[key] = key.upper()
    for i in ciphertext:
        if i.isalpha():
            i = i.lower()
            plaintext += d[i]
        else:
            plaintext += i
    return plaintext
