import cPickle
bribe=cPickle.load(open('waterwastage.p', 'rb'))
corruption=cPickle.load(open('draught.p', 'rb'))

#bmoney=cPickle.load(open('parks.p', 'rb'))


finallist=bribe+corruption#+bmoney
print len(finallist)

cPickle.dump(finallist, open('draughtcluster.p', 'wb')) 
#print str(dangerwords)
