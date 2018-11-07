import nltk
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import framenet as fn
import requests

i=0
print ('add boiling water into the cup.')
list = word_tokenize('add boiling water into the cup.')

link = 'http://api.conceptnet.io/c/en/'

i = 0
for x in list:
 for i in range(20):
    obj = requests.get(link+x).json()
    obj.keys() 
    print(obj['edges'][i])
print('word:'+x)


