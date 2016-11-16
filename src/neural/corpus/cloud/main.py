import cPickle
import numpy as np
from sklearn.svm import SVR
from sklearn import svm
from cleantweet import clean
from ordering import order
from createnumpy import buildmynumpy
def main(tweet):
	
	tweet=clean(tweet)
	tweet=order(tweet)
	
	histogram=[0,0,0,0,0,0,0,0,0,0,0,0]
	result={"railways":1,"sports":2,"defence":3,"agriculture":4,"cempowerment":5,"externalaffairs":6,"finance":7,"healthandsanitation":8,"law":9,"minority":10,"roads":11}

	
	tweet=buildmynumpy(tweet)
	
	tweet =  np.array(tweet).tolist()
	inputdata=cPickle.load(open('inputlist.p','rb'))
	#print str(inputdata[0])
	outputdata=cPickle.load(open('outputlist.p','rb'))
	#print str(outputdata[0])
	inputdata = np.array(inputdata).tolist()
	outputdata =  np.array(outputdata).tolist()
	#print str(inputdata[0])
	#print str(outputdata[0])
	#print len(inputdata)
	clf = svm.SVC(gamma=0.0000002, C=100)
	#print len(outputdata)
	"""
	j=0
	for i in range(20000,120000,30000):
		
		clf.fit(inputdata[j:i], outputdata[j:i])
		j=i
	
		x=clf.predict(list(tweet))
		print "x="+str(x)
		histogram[x]=histogram[x]+1
		
	print str(histogram)
	index= histogram.index(max(histogram))
	print index
	print list(result)[index]
	--
	clf.fit(inputdata[:50000], outputdata[:50000])
	x=clf.predict(list(tweet))
	print "x="+str(x)
	"""
	
	clf.fit(inputdata[:100000], outputdata[:100000]) 
	i=len(inputdata)
	j=100001
	ct=0
	while j<i:
		x=clf.predict(list(inputdata[j]))
		y=outputdata[j]
		if x==y:
			ct=ct+1
		#print str(clf.predict(testinputdata[j]))+ "  --  "+str(testoutputdata[j]) +"  "+str(j)
		j=j+1
	ct=ct*1.0
	print(ct/len(inputdata)*100)


	
main("Jobs by industry  #Aerospace #Defence #India http://budurl.com/WorldJobsINDIA ")

"""
10000 tweets =0m7.735s
20000 tweets =0m31.165s
25000 tweets =0m48.019s
30000 tweets =1m6.372s

50000 tweets =3m3.960s
"""
