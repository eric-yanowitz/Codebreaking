import text_functions as tf
import re

def cipher_analysis(ciphertext, top = 0, bottom = 0, n1 = 5, n2 = 5, capitals1 = False, capitals2 = False):
    frequency_analysis(ciphertext, top, bottom)
    print('')
    print(f'Missing letters: {letter_count(ciphertext)[27][1]}')
    print(f'IC: {index_of_coincidence(ciphertext)}')
    print(digraphs(ciphertext, n1, capitals1))
    print(trigraphs(ciphertext, n2, capitals2))


def letter_count(ciphertext):
    count = [['a' , 0], ['b' , 0], ['c' , 0], ['d' , 0], ['e' , 0], ['f' , 0], ['g' , 0], ['h' , 0], ['i' , 0], ['j' , 0], ['k' , 0], ['l' , 0], ['m' , 0], ['n' , 0], ['o' , 0], ['p' , 0], ['q' , 0], ['r' , 0], ['s' , 0], ['t' , 0], ['u' , 0], ['v' , 0], ['w' , 0], ['x' , 0], ['y' , 0], ['z' , 0], ['total', 0], ['missing letters', 0]]
    for i in ciphertext:
        if i.isalpha() and ord(i) < 123:
            n = ord(i.lower()) - 97
            count[n][1] += 1
            count[26][1] += 1
    for i in range(len(count) - 2):
        if count[i][1] == 0:
            count[27][1] += 1
    return count
 

# frequency of letters in ciphertext compared with the natural frequency in english
def frequency_analysis(ciphertext, top = 0, bottom = 0):
    natural_freq = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.7}
    d_count = dict.fromkeys(natural_freq.keys(), 0.0)
    d_freq = d_count
    char_count = 0
    for i in ciphertext:
        i = i.lower()
        if i in d_count:
            char_count += 1
            d_count[i] += 1
    print("Cipher Text:")
    for key in d_count:
        frequency = round(100*(d_count[key]/char_count), 1)
        d_freq[key] = frequency
        print(f'({key}) {frequency}, ', end = '')
    print("\nNatural Frequency:")
    for key, value in natural_freq.items():
        print(f'({key}) {value}, ', end = '')
    if top > 0 or bottom > 0:
        natural_freq_sorted = list(natural_freq.values())
        natural_freq_sorted.sort(reverse = True)
        d_freq_sorted = list(d_freq.values())
        d_freq_sorted.sort(reverse = True)
        print('\n\nNatural Frequency: ', end = '')
        for i in range(top):
            print(f'{natural_freq_sorted[i]}, ', end = '')
        if top > 0:
            print('/ ', end = '')
        for i in range(bottom):
            print(f'{natural_freq_sorted[len(natural_freq_sorted) - bottom + i]}, ', end = '')
        print('\nCipher Text: ', end = '')
        for i in range(top):
            print(f'{d_freq_sorted[i]}, ', end = '')
        if top > 0:
            print('/ ', end = '')
        for i in range(bottom):
            print(f'{d_freq_sorted[len(d_freq_sorted) - bottom + i]}, ', end = '')
    return


def index_of_coincidence(ciphertext):
    count = letter_count(ciphertext)
    index = 0.0
    total = count[26][1]
    denominator = total*(total-1)
    for i in range(len(count) - 2):
        j = count[i][1]
        index += (j*(j-1))/denominator
    index = index*100
    return round(index, 2)


# def match_word(cipherword, comprehensive = False, partial = False):
#     if len(cipherword) == 0:
#         return
#     if not cipherword.islower() and not cipherword.isupper():
#         partial = True
#         cipherword_t = cipherword
#     d = {}
#     regex = r""
#     flag = 1
#     d[cipherword[0]] = flag
#     regex += '(.)'
#     for i in range(1, len(cipherword)):
#         if cipherword[i] in d:
#             regex += rf'\{d[cipherword[i]]}'
#         else:
#             regex += '(?!'
#             for j in range(1, flag + 1):
#                 regex += rf'\{j}'
#             regex += ')(.)'
#             flag += 1
#             d[cipherword[i]] = flag
#     print(regex)
#     word_list = []
#     if comprehensive == True:
#         file_path = 'english_word_list_comprehensive.txt'
#     else:
#         file_path = 'english_word_list_short.txt'
#     file_content = tf.file_content(file_path, lines = True, strip = True)
#     for line in file_content:
#         if len(line) - 1 == len(cipherword):
#             match = re.search(regex, line)
#             if match:
#                 word_list.append(match.group(0))
#     if partial == False:
#         return word_list
#     else:
#         temp = word_list
#         word_list = []
#         for i in temp:
#             flag = False
#             for j in range(len(cipherword_t)):
#                 if cipherword_t[j].islower():
#                     if i[j] == cipherword_t[j]:
#                         continue
#                     else:
#                         flag = True
#                         break
#             if flag == True:
#                 continue
#             else:                
#                 word_list.append(i)
#         return word_list
    

#match word without regex's
def match_word(cipherword, comprehensive = False, partial = False):
    if comprehensive == True:
        file_path = 'english_word_list_comprehensive.txt'
    else:
        file_path = 'english_word_list_short.txt'
    file_content = tf.file_content(file_path, lines = True, strip = True)
    word_list = []
    d ={}
    if cipherword.islower() or cipherword.isupper():
        for i in range(len(cipherword)):
            if cipherword[i] not in d:
                d[cipherword[i]] = []
                d[cipherword[i]].append(i)
            else:
                d[cipherword[i]].append(i)
        for i in file_content:
            if len(i) - 1 == len(cipherword):
                s = set(i) 
                if len(s)-1 == len(d):
                    flag = False
                    for key in d:
                        if len(d[key]) > 1: 
                            for j in range(len(d[key])-1):
                                k = d[key][j]
                                l = d[key][j+1]
                                if i[k] != i[l]:
                                    flag = True
                                    break
                        if flag == True:
                            break
                    if flag == True:
                        continue
                    else:
                        word = ""
                        for n in range(len(i)-1):
                            word += i[n]
                        word_list.append(word)
    else:
        for i in range(len(cipherword)):
                if cipherword[i] not in d:
                    d[cipherword[i]] = []
                    d[cipherword[i]].append(i)
                else:
                    d[cipherword[i]].append(i)
        for i in file_content:
            if len(i) - 1 == len(cipherword):
                s = set(i) 
                if len(s)-1 == len(d):
                    flag = False
                    for key in d:
                        if key.islower():
                            for j in range(len(d[key])):
                                if i[d[key][j]] != key:
                                    flag = True
                                    break
                        else:
                            if len(d[key]) > 1: 
                                for j in range(len(d[key])-1):
                                    k = d[key][j]
                                    l = d[key][j+1]
                                    if i[k] != i[l]:
                                        flag = True
                                        break
                        if flag == True:
                            break
                    if flag == True:
                        continue
                    else:
                        word = ""
                        for n in range(len(i)-1):
                            word += i[n]
                        word_list.append(word)
    return word_list


def digraphs(ciphertext, n = 5, all = False, capitals = False):
    if capitals == True:
        cipher = ""
        for i in ciphertext:
            if i.islower():
                cipher += i
        return digraphs(cipher, n, all, capitals = False) 
    d = {}   
    for i in range(len(ciphertext)-1):
        if ciphertext[i] != ' ' and ciphertext[i+1] != ' ':
            graph = ciphertext[i] + ciphertext[i+1]
            if graph not in d:
                d[graph] = 1
            else: 
                d[graph] += 1
        else:
            continue
    dswap_list = [[value, key] for key, value in d.items()]
    dswap_list.sort(reverse = True)
    d2 ={}
    if all == True:
        for i in dswap_list:
            d2[i[1]] = i[0]
    else:
        count = 0
        for i in dswap_list:
            if count == n:
                break
            d2[i[1]] = i[0]
            count += 1
    return d2


def trigraphs(ciphertext, n = 5, all = False, capitals = False):
    if capitals == True:
        cipher = ""
        for i in ciphertext:
            if i.islower():
                cipher += i
        return trigraphs(cipher, n, all, capitals = False) 
    d = {}
    for i in range(len(ciphertext)-2):
        if ciphertext[i] != ' ' and ciphertext[i+1] != ' ' and ciphertext[i+2] != ' ':
            graph = ciphertext[i] + ciphertext[i+1] + ciphertext[i+2]
            if graph not in d:
                d[graph] = 1
            else: 
                d[graph] += 1
        else:
            continue
    dswap_list = [[value, key] for key, value in d.items()]
    dswap_list.sort(reverse = True)
    d2 ={}
    if all == True:
        for i in dswap_list:
            d2[i[1]] = i[0]
    else:
        count = 0
        for i in dswap_list:
            if count == n:
                break
            d2[i[1]] = i[0]
            count += 1
    return d2


def graphs(ciphertext, n1 = 5, n2 = 5, capitals = True):
    print(digraphs(ciphertext, n1, capitals))
    print(trigraphs(ciphertext, n2, capitals))

