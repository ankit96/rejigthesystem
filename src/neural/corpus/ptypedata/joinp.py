import cPickle
import operator

i=0
sports=cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/sports.p', 'rb'))

#data = sports + defence + railways
data = sports
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/defence.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/railways.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/agriculture.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/cempowerment.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/externalaffairs.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/finance.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/healthandsanitation.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/law.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/minority.p', 'rb')))
data.update(cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/ptypedata/roads.p', 'rb')))


cPickle.dump(data, open('basedatap.p', 'wb'))
'''
data = cPickle.load(open('/home/ankit/tweeter/src/neural/corpus/fulldata.p', 'rb'))
for a in data.keys():
	print a
'''	
