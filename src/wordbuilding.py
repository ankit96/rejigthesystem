import cPickle

obj=[]
with open('culture.txt') as f:
    for line in f:
    	if str(line[:len(line)-1]) not in obj:
        	obj.append(str(line[:len(line)-1]))
'''
print len(obj)
for a in obj:
	print str(a)
'''
cPickle.dump(obj, open('culture.p', 'wb')) 
