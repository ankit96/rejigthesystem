'''
1)for testing tweets and classifying them 
2)uses clean and classes  
'''
__author__ = 'ankit'
import cPickle
from clean import clean
from classes import stopwords
from learnandgood import learn
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
	print "cleaned"+str(x)
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
				
				key=a.keys().index(y)
				value=a.items()[key][1]
				selected.append(y)
				ct=ct+value
				
			if y[1:] in a.keys() and y[0] =='#':
				key=a.keys().index(y[1:])
				value=a.items()[key][1]
				selected.append(y)
				ct=ct+value+1
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
		
		learn(1,index,x,corr,match)
	else :
		learn(2,index,x,"null",match)
	print "--------------------------------"
	
