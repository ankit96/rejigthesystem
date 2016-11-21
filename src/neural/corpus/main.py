import cPickle
import numpy as np
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib

from cleantweet import clean
from ordering import order
from createnumpy import buildmynumpy

def main(tweet):
	tweet = clean(tweet)
	tweet = buildmynumpy(tweet)
	tweet = order(tweet)
	inputdata=cPickle.load(open('inputlist.p','rb'))
	outputdata=cPickle.load(open('outputlist.p','rb'))
	#inputdata = np.array(inputdata).tolist()
	#outputdata =  np.array(outputdata).tolist()

	clf = svm.SVC(gamma=0.0000002, C=100)
	print len(inputdata)
	try:
    		clf = joblib.load("clfobject.pkl")
    		print "using trained model"
	except:
  		print "building new model"
    		clf.fit(inputdata, outputdata)
    		joblib.dump(clf,"clfobject.pkl")
	
	
	x=clf.predict(list(tweet))
	print x
	if x==outputdata[-1]:
		print "succes"
	else:
		print "oops"
main("Manohar parikar is a good defence minister")

