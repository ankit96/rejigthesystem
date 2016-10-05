'''
1)Proper noun tagger 
Note:not working
'''
__author__ = 'ankit'
from nltk.tag import pos_tag

sentence = "Michael Jackson likes to eat at McDonalds"
tagged_sent = pos_tag(sentence.split())
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]

propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
# ['Michael','Jackson', 'McDonalds']
