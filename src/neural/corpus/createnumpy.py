import numpy as np
from ast import literal_eval
import cPickle
import operator
data=cPickle.load(open('ordereddattest.p','rb'))

traindata=[]
for a in data:
	 d=list(literal_eval(a))
	 le=len(d)
	 if le<8:
	 	d=d+ [0] * (8-le)
	 x = np.array(d[:8])
	 y = data[a]
	 z = (x , y)
	 traindata.append(z)
	 
	 
cPickle.dump(traindata, open('numpydattest.p', 'wb')) 	 
i=5
while i:
	print traindata[i]
	i=i-1
