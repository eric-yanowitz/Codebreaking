#biliteral ciphers: https://en.wikipedia.org/wiki/Bacon%27s_cipher

#given a key ('codeA'), encodes each character from the 'text' to A or B
#option to treat 'capitals' (True) as distinct from lower case
#option to encode 'onlyletters' (True) or to encode all characters (False)
#option to 'reverse' (True) the encoding so that the key ('codeA') encodes B instead of A
def biliteral_encoder(text = "", codeA = "", capitals = False, onlyletters = True, reverse = False):
    biliteral_string = ""
    text = text.replace(' ', '')
    codeA = codeA.replace(' ', '')
    if capitals == False:
        codeA = codeA.lower()
        text = text.lower()
    codeA = set(codeA)
    if onlyletters == True:
        for i in codeA:
            if not i.isalpha():
                codeA.remove(i)
    for i in text:
        if onlyletters == True and not i.isalpha():
            continue
        if i in codeA:
            if reverse == False:
                biliteral_string += 'a'
            else:
                biliteral_string += 'b'
        else:
            if reverse == False:
                biliteral_string += 'b'
            else:
                biliteral_string += 'a' 
    return biliteral_string


#converts a biliteral string to plaintext
#option to convert from the original 'latin' alphabet (True) where i/j and u/v were printed with the same character
#option to convert from 'both' (True) the modern and original latin alphabet
def interpret_biliteral(biliteral, latin = True, both = False):
    plaintext = ""
    if latin == True:
        d = {"aaaaa": "A", "aaaab": "B", "aaaba": "C","aaabb": "D", "aabaa": "E", "aabab": "F", "aabba": "G", "aabbb": "H", "abaaa": "I", "abaab": "K", "ababa": "L", "ababb": "M","abbaa": "N", "abbab": "O", "abbba": "P", "abbbb": "Q", "baaaa": "R", "baaab": "S", "baaba": "T", "baabb": "U", "babaa": "W","babab": "X", "babba": "Y", "babbb": "Z"}     
    else:
        d = {"aaaaa": "A", "aaaab": "B", "aaaba": "C","aaabb": "D", "aabaa": "E", "aabab": "F", "aabba": "G", "aabbb": "H", "abaaa": "I", "abaab": "J", "ababa": "K", "ababb": "L","abbaa": "M", "abbab": "N", "abbba": "O", "abbbb": "P", "baaaa": "Q", "baaab": "R", "baaba": "S", "baabb": "T", "babaa": "U","babab": "V", "babba": "W", "babbb": "X", "bbaaa": "Y", "bbaab": "Z"}
    if both == True:
        return interpret_biliteral(biliteral, latin = True) + '\n' + interpret_biliteral(biliteral, latin = False)
    for i in range(0, len(biliteral), 5):
        j = biliteral[i:i+5]
        if j in d:
            plaintext += d[j]
    plaintext += '\n'
    return plaintext


#given a key ('codeA' and 'codeB'), encodes each character in a 'text' to A, B, or C
#option to treat 'capitals' (True) as distinct from lower case
#option to encode 'onlyletters' (True) or to encode all characters (False)
#option 'allcodes' (True) - encodes 'text' to all 6 combinations of codeA codeB codeC, and returns a list of 6 strings
def triliteral_encoder(text = "", codeA = "", codeB = "", capitals = False, onlyletters = True, allcodes = False):
    triliteral_string = ""
    text = text.replace(' ', '')
    codeA = codeA.replace(' ', '')
    codeB = codeB.replace(' ', '')
    if capitals == False:
        text = text.lower()
        codeA = codeA.lower()
        codeB = codeB.lower()
    if onlyletters == True:
        text_temp = ""
        codeA_temp = ""
        codeB_temp = ""
        for i in text:
            if i.isalpha():
                text_temp += i
        for i in codeA:
            if i.isalpha():
                codeA_temp += i
        for i in codeB:
            if i.isalpha():
                codeB_temp += i
        text = text_temp
        codeA = codeA_temp
        codeB = codeB_temp
    codeA = set(codeA)
    codeB = set(codeB)
    for i in text:
        if i in codeA:
            triliteral_string += 'a'
        elif i in codeB:
            triliteral_string += 'b'
        else: 
            triliteral_string += 'c'
    if allcodes == True:
        t1 = triliteral_string
        t2 = ""
        t3 = ""
        t4 = ""
        t5 = ""
        t6 = ""
        for i in t1:
            if i == 'a':
                t2 += 'a'
                t3 += 'b'
                t4 += 'b'
                t5 += 'c'
                t6 += 'c'
            elif i == 'b':
                t2 += 'c'
                t3 += 'a'
                t4 += 'c'
                t5 += 'a'
                t6 += 'b'
            elif i == 'c':
                t2 += 'b'
                t3 += 'c'
                t4 += 'a'
                t5 += 'b'
                t6 += 'a'
        triliteral_strings = [t1, t2, t3, t4, t5, t6]
        return triliteral_strings
    else:
        return triliteral_string


#converts a triliteral string back to plaintext
#option to convert from the original 'latin' alphabet (True) where i/j and u/v were printed with the same character
#option to convert from 'both' (True) the modern and original latin alphabet
def interpret_triliteral(triliteral, latin = True, both = False):
    plaintext = ""
    d1 = {"aaa":"A","aab":"B","aac":"C","aba":"D","abb":"E","abc":"F","aca":"G","acb":"H","acc":"I","baa":"K","bab":"L","bac":"M","bba":"N","bbb":"O","bbc":"P","bca":"Q","bcb":"R","bcc":"S","caa":"T","cab":"U","cac":"W","cba":"X","cbb":"Y","cbc":"Z","cca": " ","ccb": " ","ccc": " "}
    d2 = {"aaa":"A","aab":"B","aac":"C","aba":"D","abb":"E","abc":"F","aca":"G","acb":"H","acc":"I","baa":"J","bab":"K","bac":"L","bba":"M","bbb":"N","bbc":"O","bca":"P","bcb":"Q","bcc":"R","caa":"S","cab":"T","cac":"U","cba":"V","cbb":"W","cbc":"X","cca":"Y","ccb":"Z", "ccc": " "}
    d = {}
    if both == True:
        return interpret_triliteral(triliteral, latin = True, both = False) + interpret_triliteral(triliteral, latin = False, both = False)
    elif latin == True:
        d = d1
    else:
        d = d2

    if type(triliteral) == str:
        for i in range(0, len(triliteral), 3):
            j = triliteral[i:i+3]
            if j in d:
                plaintext += d[j]
        plaintext += '\n'
    elif type(triliteral) == list:
        for i in range(len(triliteral)):
            triliteral_l = triliteral[i]
            plaintext += f"{i+1}: "
            for i in range(0, len(triliteral_l), 3):
                j = triliteral_l[i:i+3]
                if j in d:
                    plaintext += d[j]
            plaintext += '\n'
    return plaintext
    