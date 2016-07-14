import cPickle
railwaylist=cPickle.load(open('railways.p', 'rb'))
correct=[]
wrong=[]
for a in railwaylist:
	print a
	"""
	cor=raw_input()
	if cor=='y':
		correct.append(a)
	else:
		wrong.append(a)
		
for a in correct:
	print a
print"======"
for b in wrong:
	print b
		
		"""
