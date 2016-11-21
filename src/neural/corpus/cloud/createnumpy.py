import numpy as np
from ast import literal_eval
import cPickle


def buildmynumpy(tweet):


	a=tweet
	print a
	d=list(literal_eval(a))
	le=len(d)
	if le<8:
		d=d+ [0] * (8-le)
	x = np.array(d[:8])
	return x

