import numpy as np
from ast import literal_eval
import cPickle
import operator
data=cPickle.load(open('encodedtweets.p','rb'))

traindata=[]
ct=0
for a in data:
	 d=list(literal_eval(a))
	 le=len(d)
	 if le<8:
	 	d=d+ [0] * (8-le)
	 x = np.array(d[:8])
	 y = data[a]
	 z = (x , y)
	 traindata.append(z)
	 ct=ct+1
	 if ct>999 and ct%1000==0:
	 	print str(ct)
	 
print ct	 
cPickle.dump(traindata, open('encodednumpytweets.p', 'wb')) 	 
i=5
while i:
	print traindata[i]
	i=i-1
