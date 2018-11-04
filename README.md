# NLP-pipeline
This repository has been created for EASE project, part: H2. 

# Python Implementation
+ nlp.py takes a sentence as input and creates tuples for pos tags and frames based on FrameNet. (this code can work both in python 2.7 and python 3.6)
+ concept-extractor.py takes a sentence as input and find concepts associated with each word - based on ConceptNet. This code works in python3.


# Java Implementation
+ The first code is written in Java and JRE 8 is required.
+ The code could be executed in conjunction with Maven dependencies under "pom.xml" file.
+ In order to compile the program successfully, user needs to specify file path for the external files. 
+ External files which are listed as Containers.xml, Food.xml, Measure_volume.xml, Cause_change_of_phase.xml and Cause_fluidic_motion are the frame files based on FrameNet v.1.7, released under NLTK library.
+ verbs.txt file contains a verb list extracted from recipes, through the detection of wrong pos-taggings of one parser.
+ http://easeh2.blogspot.com/ is the blog for general nlp research.


