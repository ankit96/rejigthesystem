import cPickle
from clean import clean
from classes import stopwords
from learnandgood import learn
base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=cPickle.load(open(base+'cluster.p', 'rb'))
i=0

for a in cluster:
	if a.items()[0][0]=='stopwords':
			target=a
			cluster.remove(a)
cPickle.dump(cluster, open(base+'cluster.p', 'wb')) 
		
		
		
			
		
