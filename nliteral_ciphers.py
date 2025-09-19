def interpret_biliteral(biliteral, latin = True, both = False, danish = False):
    plaintext = ""
    if latin == True:
        d = {"aaaaa": "A", "aaaab": "B", "aaaba": "C","aaabb": "D", "aabaa": "E", "aabab": "F", "aabba": "G", "aabbb": "H", "abaaa": "I", "abaab": "K", "ababa": "L", "ababb": "M","abbaa": "N", "abbab": "O", "abbba": "P", "abbbb": "Q", "baaaa": "R", "baaab": "S", "baaba": "T", "baabb": "U", "babaa": "W","babab": "X", "babba": "Y", "babbb": "Z"}
        if danish == True:
            d['bbaaa'] = "Æ"
            d['bbaab'] = "Ø"        
    else:
        d = {"aaaaa": "A", "aaaab": "B", "aaaba": "C","aaabb": "D", "aabaa": "E", "aabab": "F", "aabba": "G", "aabbb": "H", "abaaa": "I", "abaab": "J", "ababa": "K", "ababb": "L","abbaa": "M", "abbab": "N", "abbba": "O", "abbbb": "P", "baaaa": "Q", "baaab": "R", "baaba": "S", "baabb": "T", "babaa": "U","babab": "V", "babba": "W", "babbb": "X", "bbaaa": "Y", "bbaab": "Z"}
        if danish == True:
            d['bbaba'] = "Æ"
            d['bbabb'] = "Ø"
    if both == True:
        return interpret_biliteral(biliteral, latin = True, danish = danish) + '\n' + interpret_biliteral(biliteral, latin = False, danish = danish)
    for i in range(0, len(biliteral), 5):
        j = biliteral[i:i+5]
        if j in d:
            plaintext += d[j]
    return plaintext


def biliteral_encoder(text = "", code = "", capitals = False, reverse = False, grammar = False):
    biliteral_string = ""
    text = text.replace(' ', '')
    code = code.replace(' ', '')
    if capitals == False:
        code = code.lower()
        text = text.lower()
    code = set(code)
    if grammar == False:
        for i in code:
            if not i.isalpha():
                code.remove(i)
    print(code)
    for i in text:
        if grammar == False and not i.isalpha():
            continue
        if i in code:
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