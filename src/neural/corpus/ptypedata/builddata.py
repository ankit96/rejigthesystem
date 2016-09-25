#combinning all .p type data into a huge text file which will be used for frequency matching
import cPickle
data=cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/sports.p', 'rb'))
for a in data:
	print a
	
