'''
1)converting a text file containing words into pickle format for storing list 
'''
__author__ = 'ankit'
import cPickle

obj=[]
with open('stopwords.txt') as f:
    for line in f:
    	if str(line[:len(line)-1]) not in obj:
        	obj.append(str(line[:len(line)-1]))
'''
print len(obj)
for a in obj:
	print str(a)
'''
cPickle.dump(obj, open('stopwords.p', 'wb')) 
