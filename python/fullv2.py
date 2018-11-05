import nltk
from nltk.tokenize import word_tokenize
from xml.etree import ElementTree
from pprint import pprint
from nltk.corpus import framenet as fn

list = word_tokenize('add boiling water into the cup.')
i=0

postagged =  nltk.pos_tag(list)

print('words:' + str(list))

for x in list:
    print('frame'+ '('+x+',' + str(fn.frames_by_lemma(x))+ ')')


for i in range(len(postagged)):
    print ('nltk_pos'+ str(postagged[i]))


with open('morph.xml', 'rt') as f:
    tree = ElementTree.parse(f)


with open('types.xml', 'rt') as f2:
    tree2 = ElementTree.parse(f2)


for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      pos = node.attrib.get('pos')

      if name==x:
           print ('ccg_pos'+'('+ name +  ',' + pos+')')


for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')

      if name==x:
           print ("class" +'(%s,%s)' % (name, cl))          
          
 


for node in tree.iter('entry'):
  for node2 in tree2.iter('type'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      types= node2.attrib.get('name')
      parents = node2.attrib.get('parents')

      if name==x and types ==cl:
           print ("parent"+ '(%s,%s,%s)' % (name, cl, parents))


for node in tree.iter('entry'):
  for node2 in tree2.iter('type'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      types= node2.attrib.get('name')
      parents = node2.attrib.get('parents')

      if name==x and types ==cl:
           print ("inheritance"+ '(%s,%s)' % (cl, parents))


          

