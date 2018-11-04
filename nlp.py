import nltk
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import framenet as fn

fn.frames_by_lemma('bake')
i=0
list = word_tokenize('add boiling water into the cup.')
postagged =  nltk.pos_tag(list)

print('frames:')
for x in list:
    print('('+"'"+ x+"'"+','+"'"+ str(fn.frames_by_lemma(x))+"'"+ ')')

print('postags:')
for i in range(len(postagged)):
    print (postagged[i])

print(nltk.pos_tag(list))
print(postagged[1])

print(list)
