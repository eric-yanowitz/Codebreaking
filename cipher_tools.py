import text_functions as tf
import string


#runs gamut of cipher analysis functions and presents them nicely
def cipher_analysis(ciphertext, top = 0, bottom = 0, n1 = 5, n2 = 5, capitals = True, punctuation = False):
    frequency_analysis(ciphertext, top = top, bottom = bottom)
    print('')
    print(f'Missing letters: {letter_count(ciphertext)[27][1]}')
    print(f'IC: {index_of_coincidence(ciphertext)}')
    print(digraphs(ciphertext, n = n1, capitals = capitals, punctuation = punctuation))
    print(trigraphs(ciphertext, n = n2, capitals = capitals, punctuation = punctuation))


#returns list of the counts for each english letter, total letters, and missing letters
def letter_count(ciphertext):
    count = [['a' , 0], ['b' , 0], ['c' , 0], ['d' , 0], ['e' , 0], ['f' , 0], ['g' , 0], ['h' , 0], ['i' , 0], ['j' , 0], ['k' , 0], ['l' , 0], ['m' , 0], ['n' , 0], ['o' , 0], ['p' , 0], ['q' , 0], ['r' , 0], ['s' , 0], ['t' , 0], ['u' , 0], ['v' , 0], ['w' , 0], ['x' , 0], ['y' , 0], ['z' , 0], ['total', 0], ['missing letters', 0]]
    for i in ciphertext:
        if i.isalpha() and ord(i) < 123:  #only english letters
            n = ord(i.lower()) - 97
            count[n][1] += 1
            count[26][1] += 1
    for i in range(len(count) - 2):
        if count[i][1] == 0:
            count[27][1] += 1
    return count
 

#prints frequency of each letter in the ciphertext compared with the natural frequency in english
#option to print 'top' and 'bottom' n most frequent letters 
def frequency_analysis(ciphertext, top = 0, bottom = 0):
    natural_freq = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.7}
    d_count = dict.fromkeys(natural_freq.keys(), 0.0)
    d_freq = d_count
    total = 0
    for i in ciphertext:
        i = i.lower()
        if i in d_count:
            total += 1
            d_count[i] += 1
    print("Cipher Text Frequency:")
    for key in d_count:
        frequency = round(100*(d_count[key]/total), 1)
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


#returns the Index of Coincidence of a ciphertext
#IoC for Single substitution cipher in english is around 6.67
#https://en.wikipedia.org/wiki/Index_of_coincidence
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
    

#Given a 'cipherword', returns list of all words that have the same pattern 
# (e.g. 'yfygh' will return all words of length 5 that have the same letter in the first and third position,
#  but different letters in the second, fourth, and fifth position)
# To fix certain letters, put the fixed letters in lower case and the non-fixed letters in upper case
#  (e.g. 'YFYal' will return all words of length 5 ending in 'al' that have the same letter in the first
#   and third position, and a different letter in the second position - 'rural', total', 'usual') 
#option to search from a 'comprehensive' (True) english word list or a smaller common word list (False)
def match_word(cipherword, comprehensive = False):
    if comprehensive == True:
        file_path = 'english_word_list_comprehensive.txt'
    else:
        file_path = 'english_word_list_short.txt'
    file_content = tf.file_content(file_path, lines = True, strip = True)
    word_list = []
    d ={}
    if cipherword.islower() or cipherword.isupper():   #word pattern without any fixed letters
        for i in range(len(cipherword)):
            if cipherword[i] not in d:
                d[cipherword[i]] = []
                d[cipherword[i]].append(i)
            else:
                d[cipherword[i]].append(i)
        for i in file_content:
            if len(i)-1 == len(cipherword):      #len(i)-1: file_content places '\n' char after every word
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
                        for n in range(len(i)-1):   #file_content places '\n' char after every word
                            word += i[n]
                        word_list.append(word)
    else:                                           #word pattern with fixed letters
        for i in range(len(cipherword)):
                if cipherword[i] not in d:
                    d[cipherword[i]] = []
                    d[cipherword[i]].append(i)
                else:
                    d[cipherword[i]].append(i)
        for i in file_content:
            if len(i)-1 == len(cipherword):
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


#runs digraphs and trigraphs in a single function
def graphs(ciphertext, n1 = 5, n2 = 5, capitals = True, punctuation = False):
    print(digraphs(ciphertext, n = n1, capitals = capitals, punctuation = punctuation))
    print(trigraphs(ciphertext, n = n2, capitals = capitals, punctuation = punctuation))


#returns an ordered dictionary of all digraphs and their frequency
#option to return 'n' most frequent digraphs or 'all' (True) digraphs 
# (default returns 5 most frequent digraphs)
#option to treat 'capitals' (True) as distinct from lower case
#option to include 'punctuation' marks (True) or exclude them (False)
def digraphs(ciphertext, n = 5, all = False, capitals = True, punctuation = False):
    if capitals == False:
        ciphertext = ciphertext.lower()
    if punctuation == False:
        ciphertext2 = ""
        for i in ciphertext:
            if i in string.punctuation:
                ciphertext2 += ' '
            else:
                ciphertext2 += i
        ciphertext = ciphertext2
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


#returns an ordered dictionary of all trigraphs and their frequency
#option to return 'n' most frequent trigraphs or 'all' (True) trigraphs 
# (default returns 5 most frequent digraphs)
#option to treat 'capitals' (True) as distinct from lower case
#option to include 'punctuation' marks (True) or exclude them (False)
def trigraphs(ciphertext, n = 5, all = False, capitals = True, punctuation = False):
    if capitals == False:
        ciphertext = ciphertext.lower()
    if punctuation == False:
        ciphertext2 = ""
        for i in ciphertext:
            if i in string.punctuation:
                ciphertext2 += ' '
            else:
                ciphertext2 += i
        ciphertext = ciphertext2
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
