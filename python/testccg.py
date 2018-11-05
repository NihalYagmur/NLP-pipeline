import nltk
from nltk.tokenize import word_tokenize
from xml.etree import ElementTree


list = word_tokenize('add boiling water into the cup.')

with open('morph.xml', 'rt') as f:
    tree = ElementTree.parse(f)


with open('types.xml', 'rt') as f2:
    tree2 = ElementTree.parse(f2)

print ('word-class')
for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')

      if name==x:
           print (' (%s,%s)' % (name, cl))
          
 

print ('word-class-parent_class')
for node in tree.iter('entry'):
  for node2 in tree2.iter('type'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      types= node2.attrib.get('name')
      parents = node2.attrib.get('parents')

      if name==x and types ==cl:
           print (' (%s,%s,%s)' % (name, cl, parents))


print ('child-parent')
for node in tree.iter('entry'):
  for node2 in tree2.iter('type'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      types= node2.attrib.get('name')
      parents = node2.attrib.get('parents')

      if name==x and types ==cl:
           print (' (%s,%s)' % (cl, parents))


          

