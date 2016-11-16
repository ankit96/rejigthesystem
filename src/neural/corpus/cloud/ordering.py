import cPickle
import operator
from ast import literal_eval

def order(tweet):
	i=0

	f = open("basedata.txt")
        #data.txt has a huge corpus of text which tells us the important keywords by frequency
	contents = f.read()
	f.close()
	words=tweet.split()
	
        
        diction={}
    	dictlist=[]
	for word in words:
		word=word.strip()
		if word[-1]=='s':
			word=word[:-1]
		if word[-2:]=='\'s' :
			word=word[:-2]
		diction.update({word:contents.count(word)})
		
	
  	i=0
  	out=""
	for w in sorted(diction, key=diction.get, reverse=True):
		if len(w)>3 and not w.isdigit():
	  		out=out+" " +w
	  		dictlist.append(diction[w])
	  		i=i+1
  		if i> 8:
  			break
  	return str(dictlist)

