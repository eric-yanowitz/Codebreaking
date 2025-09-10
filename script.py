import cipher_tools as ctf
import text_functions as tef
import substitution_ciphers as scf
import transposition_ciphers as tc

cryptogram = "abc defg, hi q jiklm nio pqnm e sbnbfeoim inlnb rko oabfb tu en ekfbrbha pino cik jen miwnliem pif rioa vej enm qnhoell x'yb rbbn fbemns qnoi aiw oi oegb zqjokfbh ip qbmqyqmkel hniwplegbh. qo qh en ede*bs zfijbhh. epobf oab eilomec o'll hbnm cik on en efoqjb eriko qo wqoa hidb b*edzlbh.."
print(ctf.frequency_analysis(cryptogram))
# # print(ct.index_of_coincidence(cryptogram))
print(ctf.match_word('aolOdaC'))
# print(tf.words_of_length(cryptogram, 3))
# print(sc.simple_sub_cipher(cryptogram, a ='q', i= 'e'))
print(scf.simple_sub_cipher(cryptogram, q='i', b='n', m='d', y='v', k='u', e='a', l='l'))
print(scf.simple_sub_cipher(cryptogram, q='i', b='e', g='k', m='d', y='v', k='u', e='a', l='l', n='n', j='c', i='o', o='t', p='f', w='w', c='y', r='b', a='h', h='s', f='r', z='p', t='i', u='s', x='i', s='g', d='m'))

