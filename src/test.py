'''
1)storing pickle files
'''
__author__ = 'ankit'
import cPickle
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=cPickle.load(open(base+'cluster.p', 'rb'))
for a in cluster:
	if a.items()[0][0]=="stopwords":
		print a
