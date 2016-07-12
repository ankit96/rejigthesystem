# -*- coding: utf-8 -*-
import string
from cleantweet import clean
import cPickle


output = []
f = open( 'railways.csv', 'rU' ) #open the file in read universal mode
for line in f:
    #print str(line)
    cells = line.split( ";" )
    output.append(  cells[4] ) #since we want the first, second and third column
f.close()

output=output[1:]

index=0
for tweet in output:
	tweet=clean(tweet)
	print str(tweet)
	obj=tweet.split()
	
	#if obj file present
	if index>0:
		defence=cPickle.load(open('defence.p', 'rb'))
		obj =defence + obj
	cPickle.dump(obj, open('defence.p', 'wb')) 
	index=index+1
	if index>1000:
		break

"""
culture:840
defence:6300
sports:3201
"""

