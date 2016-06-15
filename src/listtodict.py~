'''
1)opens all pickle files in dir and converts them to OrderedDict sorted in reverse order
2)appending every OrderedDict to cluster list
3)done with building ,so never run this program ever
'''
__author__ = 'ankit'

import cPickle
from collections import OrderedDict
import os
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=[]


def convert(li,name):
	d={}
	dic={}
	name=name[:-2]
	d[name]=1000
	dic=d
	for a in li:
		if a!=name:
			d[a] = 100
	d=OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))
	return d
	

p_files = [f for f in os.listdir(base) if f.endswith('.p')]
#print p_files
i=0
for a in p_files:
	x=convert(cPickle.load(open(base+a, 'rb')),a.lower())
	cluster.append(x)
'''
for a in cluster:
	a=OrderedDict(a)
	print a
	print str(a.items()[0][1])
	cluster[i].insert(0,a[:-2])
	i=i+1'''
