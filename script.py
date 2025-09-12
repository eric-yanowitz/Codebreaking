import cipher_tools as ctf
import text_functions as tef
import substitution_ciphers as scf
import transposition_ciphers as tc

cryptogram = "wno za jyv yva ynkhv rau wno xkrguzax jyv yva ynkhv rgv jyv hriv. jykh, yv myn nmah jyv yva ynkhv ikhj sv uvrw, sbzau, ng snjy."
print(ctf.frequency_analysis(cryptogram))
print(ctf.index_of_coincidence(cryptogram))
print(ctf.match_word('SBint'))
print(tef.words_of_length(cryptogram, 3))
print(scf.substitution_cipher(cryptogram, j='s', y='o', v='n', a='e', n='f', k='t', h='e'))
print(scf.substitution_cipher(cryptogram, wno='fox', yva='hen', za ='in', ynkhv= 'house', ynkh= 'hous'))




