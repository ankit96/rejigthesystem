'''
1)opens all list objects stored in directory and appends to a common list called cluster
2)opens a list for stopords
'''
__author__ = 'ankit'
import cPickle
import os
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=[]



p_files = [f for f in os.listdir(base) if f.endswith('.p')]
#print p_files
i=0
for a in p_files:
	cluster.append(cPickle.load(open(base+a, 'rb')))
	cluster[i].insert(0,a[:-2])
	i=i+1
stopwords=cPickle.load(open(base+'stopwords.p', 'rb'))
	
'''
for a in cluster:
	print a

science=cPickle.load(open(base+'science.p', 'rb'))

HR=cPickle.load(open(base+'HR.p', 'rb'))
Railways=cPickle.load(open(base+'Railways.p', 'rb'))
Defence=cPickle.load(open(base+'Defence.p', 'rb'))
Minority=cPickle.load(open(base+'Minority.p', 'rb'))
socialjustice=cPickle.load(open(base+'socialjustice.p', 'rb'))


science.insert(0,'science')
HR.insert(0,'HR')
socialjustice.insert(0,'socialjustice')
Railways.insert(0,'railways')
Defence.insert(0,'defence')
Minority.insert(0,'minority')


cluster.append(science)
cluster.append(Railways)
cluster.append(Defence)
cluster.append(Minority)
cluster.append(HR)
cluster.append(socialjustice)
'''



