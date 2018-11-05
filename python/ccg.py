import nltk
from nltk.tokenize import word_tokenize
from xml.etree import ElementTree


list = word_tokenize('add boiling water into the cup.')

with open('morph.xml', 'rt') as f:
    tree = ElementTree.parse(f)


for node in tree.iter('entry'):
    for x in list:
      name = node.attrib.get('word')
      cl = node.attrib.get('class')
      if name==x:
           print (' (%s, %s )' % (name, cl))
     
