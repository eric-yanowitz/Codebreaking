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
        if skip_count != 0:
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

# frequency of letters in ciphertext compared with the natural frequency in english
def frequency_analysis(ciphertext):
    natural_frequency = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.7}
    d = dict.fromkeys(natural_frequency.keys(), 0.0)
    char_count = 0
    for i in ciphertext:
        if i in d:
            char_count += 1
            d[i] += 1
    for key in d:
        frequency = round(100*(d[key]/char_count), 1)
        print(f'({key}: {frequency}%) ', end = '')
    print("\n\nnatural frequency:")
    for key, value in natural_frequency.items():
        print(f'({key}: {value}%) ', end = '')

      
ciphertext = "qcbufohizohs mci. ^i do not^ tcfush ^but^ hvwby ^of you^ jsfm aiqv ^and^ kcbrsf ^if we^ gvozzassh wbgwl cfgsjsb kssyg.\n\n^am so looking forward to it.^ Kobhhc gssmci acfs hvob wqob hszzmci. ^Will^ zsh ybck ^in^ opcih twjs kssyg hwas \n\nGvozz kowh dcfhzobr rd ghohwcb hvifgrom twjs qzcqy gvcizr aiqv zwys gssmci."
# frequency_analysis(ciphertext)
print(caesar_decipher(ciphertext, 14, False, True))

