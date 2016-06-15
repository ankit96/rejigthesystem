'''
1)for testing tweets and classifying them 
2)uses clean and classes  
'''
__author__ = 'ankit'
import cPickle
from clean import clean
from classes import stopwords
from learnandgood import good
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=cPickle.load(open(base+'cluster.p', 'rb'))
match=[]
selected=[]
while(1):
	inp=raw_input()
	inp=inp.lower()
	x=inp.split()
	#print x
	x=clean(x)
	words=x
	print x
	maxct=0
	for a in cluster:
		selected=[]
		ct=0
		#print len(a)
		s='#'+a.items()[0][0]
		if a.items()[0][0] in x or s in x:
			index=a.items()[0][0]
			break
		for y in x:
			#print y\
			
			if y in a.keys():
				ct=ct+1
				selected.append(y)
				
			if y[1:] in a.keys() and y[0] =='#':
				ct=ct+2
				selected.append(y)
		#print ct
		if ct> 0:
			lis=[]
			lis.append(a.items()[0][0])
			lis=lis+selected
			match.append(lis)
		if ct>maxct:
			maxct=ct
			index=a.items()[0][0]
		
	print str(index)
	
	correct=raw_input()
	if correct=='n':
		corr=raw_input()
		learn(corr,index)
	else :
		good(index,x,match)
	
