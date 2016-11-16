import cPickle
import numpy as np
from sklearn.svm import SVR


data = cPickle.load(open('numpyfulldata.p','rb'))
print len(data)
training_data=data[:40000]
test_data =data[40001:]
inputdata=[]
outputdata=[]
for a in training_data:
	inputdata.append(a[0])
	outputdata.append(a[1])
testinputdata=[]
testoutputdata=[]	
for a in test_data:
	testinputdata.append(a[0])
	testoutputdata.append(a[1])
print str(outputdata[0])
from sklearn import svm

clf = svm.SVC(gamma=0.0000002, C=100)
clf.fit(inputdata, outputdata) 
i=len(testinputdata)
j=0
ct=0
while j<i:
	x=clf.predict(list(testinputdata[j]))
	y=testoutputdata[j]
	if x==y:
		ct=ct+1
	#print str(clf.predict(testinputdata[j]))+ "  --  "+str(testoutputdata[j]) +"  "+str(j)
	j=j+1
ct=ct*1.0
print(ct/len(testinputdata)*100)

