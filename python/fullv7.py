import nltk
from nltk.tokenize import word_tokenize
from xml.etree import ElementTree
from pprint import pprint
from nltk.corpus import framenet as fn

punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sent = input("Enter the sentence: ")


no_punct = ""
for char in sent:
   if char not in punct:
       no_punct = no_punct + char

list = word_tokenize(no_punct.lower())
i=0

postagged =  nltk.pos_tag(list)

print('{')
print('"analysis": ')

print('{')
print('"words": ' + str(list))
print('"frames":')
print('[')
for x in list:
    print('('+x+','+ str(fn.frames_by_lemma(x))+ ')')
print(']')

with open('morph.xml', 'rt') as f:
    tree = ElementTree.parse(f)


with open('types.xml', 'rt') as f2:
    tree2 = ElementTree.parse(f2)


print ('"nltk_pos":')
print('[')
for i in range(len(postagged)):
    print (str(postagged[i]))
print(']')  

print('"ccg_pos":')
print('[')
for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      pos = node.attrib.get('pos')

      if name==x:
           print ('('+x+','+ pos+')')
print(']')      

print('"class":')
print('[')
for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')

      if name==x:
           print ('('+x+',' + str(cl) + ')')          
print(']')                
 

print('"parent":')
print('[')
for node in tree.iter('entry'):
  for node2 in tree2.iter('type'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      types= node2.attrib.get('name')
      parents = node2.attrib.get('parents')

      if name==x and types ==cl:
           print ('(' +x+','+ str(parents) + ')')
print(']')  

print('}')
print('}')

