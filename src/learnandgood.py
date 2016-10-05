from collections import OrderedDict
import os
import cPickle
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=cPickle.load(open(base+'cluster.p', 'rb'))

def incorrect(name,li):
	for order in cluster:
		if order.items()[0][0]==name:
			target=order
			cluster.remove(order)
			break

	for b in li:
	
		#print b
		if b in target.keys():
			key=target.keys().index(b)
			value=target.items()[key][1]
			target.update({b:value-1})
	target=OrderedDict(sorted(target.items(), key=lambda t: t[1], reverse=True))
	cluster.append(target)

def correct(correct,words):
	for order in cluster:
		if order.items()[0][0]==correct:
			target=order
			cluster.remove(order)
			break
		'''	
	for m in ['child','development','girl','boy','innocent','labour']:
		target.update({m:500})
		'''
			
	for b in words:
		
		if b not in target.keys():
			#print b
			target.update({b:100})
			
			
			
		else:
			#print b
			
			key=target.keys().index(b)
			value=target.items()[key][1]
			target.update({b:value+1})
			
	target=OrderedDict(sorted(target.items(), key=lambda t: t[1], reverse=True))
	#print target
	cluster.append(target)
		

	
def learn(code,index,x,corr,match):
	if code ==2:
		
		correct(index,x)
		for a in match:
			if a[0]!=index:
				incorrect(a[0],a[1:])
	else :
		correct(corr,x)
		for a in match:
			if a[0]!=corr:
				incorrect(a[0],a[1:])
	#print cluster
	cPickle.dump(cluster, open(base+'cluster.p', 'wb')) 
		
#good("defence",['manohar', 'parrikar', 'hails', 'all-girl', 'ncc', 'team', 'everest'])
