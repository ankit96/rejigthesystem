import cPickle
import operator
i=0
data=cPickle.load(open('dattest.p', 'rb'))
#data contains a dictionary having tweets as keys and category as value
'''
text = open('data.txt').read().replace('ht/', '')
print text
'''
from ast import literal_eval

def order(tweet):
	words=tweet.split()
	
        f = open("data.txt")
        #data.txt has a huge corpus of text which tells us the important keywords by frequency
        contents = f.read()
        f.close()
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
newdict={}
result={"railways":1,"sports":2,"defence":3}

for a in data:
	
	newdict.update({order(a):result[data[a]]})
cPickle.dump(newdict, open('ordereddat.p', 'wb')) 	
'''
for a in newdict:
	x = list(literal_eval(a))
	for b in x:
		print b
	print("---------------")
	print newdict[a]
	break
'''
