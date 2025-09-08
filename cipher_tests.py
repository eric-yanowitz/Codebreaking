# frequency of letters in ciphertext compared with the natural frequency in english
def frequency_analysis(ciphertext, top = 0, bottom = 0, count = False):
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

def index_of_coincidence(ciphertext):
    return