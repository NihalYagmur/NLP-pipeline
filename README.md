# NLP-pipeline
This repository has been created for EASE project, part: H2. 
+ http://easeh2.blogspot.com/ is the blog for general nlp research.

# Implementation with R
Some codes for statistical analysis on text exist in R folder. Connection between text and machine learning is also considered.

# Python Implementation
+ nlp.py takes a sentence as input and creates tuples in the form (word,pos tag) and (word, frame)  based on the frames in FrameNet. (this code can both work in python 2.7 and python 3.6)
+ concept-extraction.py takes a sentence as input and find concepts associated with each word - based on ConceptNet. This code works in python3. The output is in JSON format.
+ ccg.py takes a sentence as input and finds the associated matches for the words from morph.xml file (openccg).
+ testccg.py takes a sentence as input and finds the relations from morph.xml and types.xml files, creating tuples and triples.
+ fullv2.py takes a sentence as input and connects all relations.
+ dandelion.py takes the text as input and extracts entities from the text through Dandelion API.
+ fullv5.py and fullv7.py takes a sentence as input and returns a formatted data.
+ fullv8.py takes a sentence as input and returns formatted data (named entity recognition added, with Spacy library.)
+ final.py is the file with the final structure (contains frames based on Framenet, pos-tags,named entity recognition, ccg-tags referring to ontospace ontology and the grammar library.)
+ combination.py prints combinations of words in sentence.
+ ngram.py prints n-grams in sentences.

# Java Implementation
+ App.java has been written in Java and JRE 8 is required.
+ The code could be executed in conjunction with Maven dependencies under "pom.xml" file.
+ In order to compile the program successfully, user needs to specify file path for the external files. 
+ External files which are listed as Containers.xml, Food.xml, Measure_volume.xml, Cause_change_of_phase.xml and Cause_fluidic_motion are the frame files based on FrameNet v.1.7, released under NLTK library.
+ verbs.txt file contains a verb list extracted from recipes, through the detection of wrong pos-taggings of one parser.



