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
f = open( 'railways.csv', 'rU' ) #open the file in read universal mode
for line in f:
    #print str(line)
    cells = line.split( ";" )
    output.append(  cells[4] ) #since we want the first, second and third column
f.close()
obj=[]
output=output[1:]


for tweet in output:
	tweet=clean(tweet)
	print str(tweet)
	'''
	inp=raw_input()
	if inp=='y':
		cortext_file.write(tweet)
	else:
		incortext_file.write(tweet)
	obj=obj+tweet.split()
	'''
	#data.update({tweet:'railways'})
	
	

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

