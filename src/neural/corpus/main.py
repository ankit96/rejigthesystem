import cPickle
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
training_data = cPickle.load(open('traindata.p','rb'))
test_data = cPickle.load(open('numpydattest.p','rb'))
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

from sklearn import svm

clf = svm.SVC(gamma=0.0000002, C=100)
clf.fit(inputdata, outputdata) 
'''
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(inputdata, outputdata).predict(inputdata)
y_lin = svr_lin.fit(inputdata, outputdata).predict(inputdata)
y_poly = svr_poly.fit(inputdata, outputdata).predict(inputdata)
plt.scatter(X, y, c='k', label='data')

plt.hold('on')
plt.plot(X, y_rbf, c='g', label='RBF model')
plt.plot(X, y_lin, c='r', label='Linear model')
plt.plot(X, y_poly, c='b', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
'''
i=len(testinputdata)
j=0
ct=0

while j<i:
	x=clf.predict(testinputdata[j])
	y=testoutputdata[j]
	if x==y:
		ct=ct+1
	#print str(clf.predict(testinputdata[j]))+ "  --  "+str(testoutputdata[j]) +"  "+str(j)
	j=j+1
print float(ct)/len(testinputdata)*100

'''
import neuralnet
net = neuralnet.Network([8, 8, 3])

net.SGD(training_data, 30, 10, 3, test_data)



import network2
net = network2.Network([8, 8, 3], cost=network2.CrossEntropyCost)
net.large_weight_initializer()


net.SGD(training_data, 100, 10, 0.3,evaluation_data=test_data, lmbda =  5.0,monitor_evaluation_accuracy=True,monitor_training_cost=True, monitor_training_accuracy=True)
'''
