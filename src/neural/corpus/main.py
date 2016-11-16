import cPickle
import numpy as np
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib

def main(tweet):
	
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
    		clf.fit(inputdata[:-2], outputdata[:-2])
    		joblib.dump(clf,"clfobject.pkl")
	
	
	x=clf.predict(list(inputdata[-1]))
	if x==outputdata[-1]:
		print "succes"
	else:
		print "oops"
main("yo")

