import cipher_tools as ct
import text_functions as te
import substitution_ciphers as sc
import nliteral_ciphers as nlc

cryptogram = "to see clearly is a beautiful X"

# n = nlc.triliteral_encoder(cryptogram, codeA = 'tawoihfbs', codeB = 'cfgjklmnpqyz', allcodes = True)
# print(nlc.interpret_triliteral(n))
# n = nlc.biliteral_encoder(cryptogram, code = 'aeiou')
# n2 = nlc.biliteral_encoder(cryptogram, code = 'aeiou', reverse = True)
# print(nlc.interpret_biliteral(n, both = True))
# print(nlc.interpret_biliteral(n2, both = True))
# d = {'total': 0}
# for key, value in ct.digraphs(cryptogram, all = True).items():
#     if key[0] == key[1]:
#         d['total'] += value
#         d[key] = value
# print(d)
# ct.cipher_analysis(cryptogram)
# print(ct.letter_count(cryptogram))
n = nlc.biliteral_encoder(cryptogram, code = 'toaclrib')
print(nlc.interpret_biliteral(n, both = True))

