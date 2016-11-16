import cPickle
import numpy as np
from sklearn.svm import SVR
from sklearn import svm

def main(tweet):
	inputlist=[]
	outputlist=[]
	data=cPickle.load(open('encodednumpytweets.p','rb'))
	for a in data:
		inputlist.append(a[0])
		outputlist.append(a[1])
	cPickle.dump(inputlist, open('inputlist.p', 'wb'))
	cPickle.dump(outputlist, open('outputlist.p', 'wb')) 	
	
main("yo")

