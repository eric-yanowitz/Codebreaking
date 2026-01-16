#caeser cipher: https://en.wikipedia.org/wiki/Caesar_cipher
#substitution cipher: https://en.wikipedia.org/wiki/Substitution_cipher

import string

#given a 'key' number, deciphers a caesar cipher text (key pushes the plaintext 
# alphabet forward x spaces i.e. pushes the substitution alphabet backwards x spaces)
#option for 'abbreviated' decipher result (first 25 characters) 
#option for 'partial' decipher - letters between the '^' character in the cryptogram are
# not deciphered i.e. inserted without change into the plaintext result
def caesar_cipher(ciphertext, key = 0, abbreviated = False, partial = False):
    plaintext = ""
    if key > 25 or key < -25:
        plaintext = "Invalid key number"
        return plaintext
    if key < 0:
        key = 26 + key
    
    skip_count = 0
    for i in range(len(ciphertext)):
        if abbreviated == True and i == 25:
            break
        
        j = ciphertext[i]

        if partial == True and skip_count != 0:      #iterates/skips the chars in between '^'s and the closing '^'
            skip_count -= 1
            continue
        if partial == True and j == "^":             
            index = i + 1                           
            while ciphertext[index] != "^":
                plaintext += ciphertext[index]       #adding the cipher letters between '^'s unchanged to the plaintext
                index += 1
                skip_count += 1                      #skip_count will equal the number of letters in between '^'s
            skip_count += 1                          #skip_count adds 1 for the closing '^'
            continue                                 #opening '^' will be skipped

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


#caesar cipher exhaustive - deciphers caeser cipher text for all 25 keys
#for options 'abbreviated' and 'partial' refer to caeser_cipher function
def caesar_cipher_ex(ciphertext, abbreviated = False, partial = False):
    plaintext = ""
    for i in range(0, 26):
        plaintext += f"key = {i}: "
        plaintext += caesar_cipher(ciphertext, i, abbreviated, partial)
        plaintext += "\n\n"
    return plaintext


#given a key, performs a substitution on the ciphertext
#the key(s) are given as multiple key='value' pairs or a single pair
# (e.g. i='a', b='f', l='e' or ibl='afe' - both are the same)
# a single-character key can have a multiple character value (e.g. i='th' or &='to')
def substitution_cipher(ciphertext, **kwargs):
    plaintext = ""
    d = dict.fromkeys(string.ascii_lowercase, '')
    for key, value in kwargs.items():
        if len(key) == len(value):
            for i in range(len(key)):         
                if key[i].isalpha():
                    t = key[i].lower()
                    d[t] = value[i].lower()
                else:
                    d[key[i]] = value[i].lower()
        else:                                     #len(key) == 1
            if key.isalpha():                 
                key = key.lower()
                d[key] = value.lower()
            else:
                d[key] = value.lower()
    for key in d:
        if len(d[key]) == 0:
            d[key] = key.upper()
    for i in ciphertext:
        if i.isalpha():
            i = i.lower()
        if i in d:
            plaintext += d[i]
        else:
            plaintext += i
    return plaintext


