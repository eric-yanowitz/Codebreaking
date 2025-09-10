import text_functions as tf
import re

# frequency of letters in ciphertext compared with the natural frequency in english
def frequency_analysis(ciphertext, top = 0, bottom = 0, show_freq = True, show_count = False):
    natural_freq = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.7}
    d_count = dict.fromkeys(natural_freq.keys(), 0.0)
    d_freq = d_count
    char_count = 0
    for i in ciphertext:
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


def letter_count(ciphertext):
    count = [['a' , 0], ['b' , 0], ['c' , 0], ['d' , 0], ['e' , 0], ['f' , 0], ['g' , 0], ['h' , 0], ['i' , 0], ['j' , 0], ['k' , 0], ['l' , 0], ['m' , 0], ['n' , 0], ['o' , 0], ['p' , 0], ['q' , 0], ['r' , 0], ['s' , 0], ['t' , 0], ['u' , 0], ['v' , 0], ['w' , 0], ['x' , 0], ['y' , 0], ['z' , 0], ['total', 0]]
    for i in ciphertext:
        if i.isalpha():
            n = ord(i.lower()) - 97
            count[n][1] += 1
            count[26][1] += 1
    return count



def index_of_coincidence(ciphertext):
    count = letter_count(ciphertext)
    index = 0.0
    total = count[26][1]
    denominator = total*(total-1)
    for i in range(len(count) - 1):
        j = count[i][1]
        index += (j*(j-1))/denominator
    index = index*100
    return round(index, 2)


def match_word(cipherword, short_list = False):
    cipherword = cipherword.lower()
    d = {}
    regex = r""
    index = 1
    d[cipherword[0]] = [index, True, 0]
    for i in range(1, len(cipherword)):
        if cipherword[i] not in d:
            index += 1
            d[cipherword[i]] = [index, False, 0]
        else:
            d[cipherword[i]][1] = True
            d[cipherword[i]][2] += 1
    for i in range(len(cipherword)):
        if d[cipherword[i]][0] == 1 and d[cipherword[i]][1] == True:
            regex += '(.)'
            d[cipherword[i]][1] = False
        elif d[cipherword[i]][1] == True and d[cipherword[i]][0] != 1:
            regex += '(?!'
            for i in range(d[cipherword[i]][0] - 1):
                i += 1
                regex += rf'\{i}'
            regex += ')(.)'
            d[cipherword[i]][1] = False
        elif d[cipherword[i]][1] == False and d[cipherword[i]][2] > 0:
            regex += rf'\{d[cipherword[i]][0]}'
            d[cipherword[i]][2] -= 1        
        else:
            regex += '(?!'
            for i in range(d[cipherword[i]][0] -1):
                i += 1
                regex += rf'\{i}'
            regex += ')(.)'
    word_list = []
    print(regex)
    if short_list == True:
        file_path = 'english_word_list_short.txt'
    else:
        file_path = 'english_word_list.txt'
    file_content = tf.file_content(file_path, lines = True, strip = True)
    for line in file_content:
        if len(line) - 1 == len(cipherword):
            match = re.search(regex, line)
            if match:
                word_list.append(match.group(0))
    return word_list


print(match_word('horror'))