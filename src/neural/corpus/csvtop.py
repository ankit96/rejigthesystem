# -*- coding: utf-8 -*-
import string
from cleantweet import clean
import cPickle

def f1(seq):
   # not order preserving
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

output = []
f = open( '/home/ankit/tweeter/src/neural/corpus/sports/output_got12.csv', 'rU' ) #open the file in read universal mode
for line in f:
    #print str(line)
    cells = line.split( ";" )
    output.append(  cells[4] ) #since we want the first, second and third column
f.close()
obj=[]
output=output[1:]

index=0
array=[]
data=cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/sports/sports.p', 'rb'))
#data={}
for tweet in output:
	tweet=clean(tweet)
	#print str(tweet)
	'''
	inp=raw_input()
	if inp=='y':
		cortext_file.write(tweet)
	else:
		incortext_file.write(tweet)
	obj=obj+tweet.split()
	'''
	data.update({tweet:'sports'})
	
	

cPickle.dump(data, open('/home/ankit/tweeter/src/neural/corpus/sports/sports.p', 'wb'))
'''
i=0
data1=cPickle.load(open('datatest.p', 'rb'))
for a in data1:
	print a
	print data[a]
	i=i+1
	if i>5:
		break
'''
"""
	if index>0:
		defence=cPickle.load(open('e.p', 'rb'))
		obj =defence + obj
	cPickle.dump(obj, open('defence.p', 'wb')) 
	index=index+1
	
	if index>10:
		break
	
cortext_file.close()
incortext_file.close()

culture:840
defence:6300
sports:3201
"""

