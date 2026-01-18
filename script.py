import cipher_tools as ct
import text_functions as tf
import substitution_ciphers as sc
import nliteral_ciphers as nlc

#caesar cipher:
# 1.) qcbufohizohs mci. ^i do not^ tcfush ^but^ hvwby ^of you^ jsfm aiqv ^and^ kcbrsf ^if we^ gvozzassh wbgwl cfgsjsb kssyg.\n\n^am so looking forward to it.^ Kobhhc gssmci acfs hvob wqob hszzmci. ^Will^ zsh ybck ^in^ opcih twjs kssyg hwas \n\nGvozz kowh dcfhzobr rd ghohwcb hvifgrom twjs qzcqy gvcizr aiqv zwys gssmci.
#   solution: key = 14

cryptogram = "qcbufohizohs mci. ^i do not^ tcfush ^but^ hvwby ^of you^ jsfm aiqv ^and^ kcbrsf ^if we^ gvozzassh wbgwl cfgsjsb kssyg.\n\n^am so looking forward to it.^ Kobhhc gssmci acfs hvob wqob hszzmci. ^Will^ zsh ybck ^in^ opcih twjs kssyg hwas \n\nGvozz kowh dcfhzobr rd ghohwcb hvifgrom twjs qzcqy gvcizr aiqv zwys gssmci."

print(ct.letter_count(cryptogram), '\n')
ct.frequency_analysis(cryptogram)
print('\n')
print(ct.index_of_coincidence(cryptogram), '\n')
print(ct.digraphs(cryptogram), '\n')
print(ct.trigraphs(cryptogram), '\n')

print(ct.match_word('qcbufohizohs', comprehensive = True), '\n')

print(sc.caesar_cipher(cryptogram, key = 14, partial = True), '\n\n')
#print(sc.caesar_cipher_ex(cryptogram, partial = True), '\n')


#substituion cipher:
# 3.) cryptogram: uwckwccbsd ex kzw owvvbcy ex wdbrwtwkz scv obddbsj 1917 * xhbwvjsc * 2017
# solution: u='c', w='e', c='n', k='t', b='i', s='a', d='l', e='o', x='f', o='w', v='d', y='g', r='z', t='b', z='h', j='m', h='r'
# solution text: centennial of the wedding of elizebeth and william 1917 * friedman * 2017

cryptogram = 'uwckwccbsd ex kzw owvvbcy ex wdbrwtwkz scv obddbsj 1917 * xhbwvjsc * 2017'

ct.cipher_analysis(cryptogram)
print(ct.match_word('uwckwccbsd', comprehensive = True), '\n')
print(sc.substitution_cipher(cryptogram, uwckwccbsd = 'centennial'), '\n')

print(ct.match_word('OilliaJ'), '\n')

print(sc.substitution_cipher(cryptogram, uwckwccbsd = 'centennial', oj='wm'), '\n')

print(sc.substitution_cipher(cryptogram, uwckwccbsd = 'centennial', oj='wm', ex='of', z='h', vy ='dg', rtz = 'zbh', xhv ='frd'), '\n')


#biliteral cipher:
# cryptogram: To enCOde A mesSage eACh letter OF the PLaIntEXt Is replaced bY A GrouP OF FiVE oF The lETteRS 'A' OR 'B'.
# plaintext: 'steganography'
# codeA = all lower case letters -> codeB = all upper case letters

cryptogram = "To enCOde A mesSage eACh letter OF the PLaIntEXt Is replaced bY A GrouP OF FiVE oF The lETteRS 'A' OR 'B'."

biliteral = nlc.biliteral_encoder(cryptogram, codeA = 'abcdefghijklmnopqrstuvwxyz', capitals = True)
print(nlc.interpret_biliteral(biliteral, latin = True))
biliteral = nlc.biliteral_encoder(cryptogram, codeA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', capitals = True, reverse = True)
print(nlc.interpret_biliteral(biliteral, latin = True))



#triliteral cipher:
# cryptogram: A short tRilITeral
# plaintext: 'hello'
# code_A = 'AoRI', code_B = 'hrtlec' -> code_C = remaining letters

cryptogram = "A short tRilITeral"
triliteral = nlc.triliteral_encoder(cryptogram, codeA = "AoRI", codeB = "hrtlec", capitals = True)
print(nlc.interpret_triliteral(triliteral, latin = False))

code_A = 'AoRI'
code_B = 'hrtlec'
code_C = 'siTa'
triliteral = nlc.triliteral_encoder(cryptogram, codeA = code_C, codeB = code_A, capitals = True, allcodes = True)
print(nlc.interpret_triliteral(triliteral, latin = False))