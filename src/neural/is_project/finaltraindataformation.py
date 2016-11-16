import cPickle
import numpy as np



data = cPickle.load(open('numpyfulldata.p','rb'))
training_data=data[:40000]
test_data =data[40001:]
inputdata=[]
outputdata=[]
for a in data:
	inputdata.append(a[0])
	outputdata.append(a[1])

cPickle.dump(inputdata, open('inputfinaldata.p', 'wb'))
cPickle.dump(outputdata, open('outputfinaldata.p', 'wb'))

