from collections import OrderedDict
import os
import cPickle
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=cPickle.load(open(base+'cluster.p', 'rb'))

def learn(name,li):
	for order in cluster:
		if order.items()[0][0]==name:
			target=order
			cluster.remove(order)
			break
	'''for a in p_files:
		if correct==a[:-2]:
			y=cPickle.load(open(base+a, 'rb'))
	'''
	
	for b in li:
	
		#print b
		if b in target.keys():
			key=target.keys().index(b)
			value=target.items()[key][1]
			target.update({b:value-1})
	target=OrderedDict(sorted(target.items(), key=lambda t: t[1], reverse=True))
	cluster.append(target)
	
def good(correct,words,match):
	
	#p_files = [f for f in os.listdir(base) if f.endswith('.p')]
	#words=['manohar', 'parrikar', 'hails', 'all-girl', 'ncc', 'team', 'everest']
	for a in match:
		if a[0]!=correct:
			learn(a[0],a[1:])
	for order in cluster:
		if order.items()[0][0]==correct:
			target=order
			cluster.remove(order)
			break
	'''for a in p_files:
		if correct==a[:-2]:
			y=cPickle.load(open(base+a, 'rb'))
	'''
	
	for b in words:
	
		if b not in target.keys():
			#print b
			target.update({b:100})
		else:
			print b
			key=target.keys().index(b)
			value=target.items()[key][1]
			target.update({b:value+1})
	target=OrderedDict(sorted(target.items(), key=lambda t: t[1], reverse=True))
	cluster.append(target)
	'''for a in cluster:
		if a.items()[0][0]==correct:
			print a
			'''
	#print cluster
	#y=convert(y,correct)
	#cluster.append(y)
	cPickle.dump(cluster, open(base+'cluster.p', 'wb')) 
	
	
#good("defence",['manohar', 'parrikar', 'hails', 'all-girl', 'ncc', 'team', 'everest'])
