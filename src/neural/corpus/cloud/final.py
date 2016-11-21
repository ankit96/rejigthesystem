import cPickle
from sklearn import svm
from sklearn.externals import joblib

from cleantweet import clean
from ordering import order
from createnumpy import buildmynumpy

def main(tweet):
	tweet = clean(tweet)
	#print tweet
	f = open("basedata.txt")
        #data.txt has a huge corpus of text which tells us the important keywords by frequency
	contents = f.read()
	f.close()
	'''	
	for a in tweet.split():
		
		print str(a)+" = "+str(contents.count(a))
	'''
	tweet = order(tweet)
	#print "hey "+str(tweet)
	#tweet = [1654, 392, 372, 270, 10]
	


	tweet = buildmynumpy(tweet)
	#print "vaka"+str(tweet)
	
	inputdata=cPickle.load(open('inputlist.p','rb'))
	outputdata=cPickle.load(open('outputlist.p','rb'))
	#inputdata = np.array(inputdata).tolist()
	#outputdata =  np.array(outputdata).tolist()

	clf = svm.SVC(gamma=0.0000002, C=100)
	#print len(inputdata)
	try:
    		clf = joblib.load("clfobject.pkl")
    		#print "using trained model"
	except:
  		#print "building new model"
    		clf.fit(inputdata, outputdata)
    		joblib.dump(clf,"clfobject.pkl")
	
	#print tweet
	x=clf.predict(list(tweet))
	#print x
	outputlist=["railways","sports","defence","agriculture","cempowerment","externalaffairs","finance","healthandsanitation","law","minority","roads"]

	#print outputlist[x-1]
	return "#"+str(outputlist[x-1])
#main("Indian Defence")


