
import cPickle

base='/home/ankit/tweeter/corpus/clusters/goverment/'
cluster=[]

science=cPickle.load(open(base+'science.p', 'rb'))

HR=cPickle.load(open(base+'HR.p', 'rb'))
Railways=cPickle.load(open(base+'Railways.p', 'rb'))
Defence=cPickle.load(open(base+'Defence.p', 'rb'))
Minority=cPickle.load(open(base+'Minority.p', 'rb'))
socialjustice=cPickle.load(open(base+'socialjustice.p', 'rb'))


science.insert(0,'science')
HR.insert(0,'HR')
socialjustice.insert(0,'socialjustice')
Railways.insert(0,'railways')
Defence.insert(0,'defence')
Minority.insert(0,'minority')


cluster.append(science)
cluster.append(Railways)
cluster.append(Defence)
cluster.append(Minority)
cluster.append(HR)
cluster.append(socialjustice)
stopwords=cPickle.load(open(base+'stopwords.p', 'rb'))

def clean(parliament):
	redundant=[':',",",")",".","(",";","/","|","-",'?','=','+']
	i=0
	flag=0
	newobj=[]
	print parliament
	for a in parliament:
		#print a
		'''if a=='...':
			flag=1
			'''
		while a[-1] in redundant:
			if len(a)>1:
				a=a[:-1]
				'''if flag==1:
					print a +str(i)
					'''
			else:
		
				#print a
				a="n"
				#parliament.pop(i)
		while a[0] in redundant:
			if len(a)>1:
				a=a[1:]
			else:
				a="n"
		
		if ',' in a:
			b=a.split(',')
			flag=1
		if a =='n':
			parliament.pop(i)
		else:
		
			if flag==1:
				for m in b:
					if m not in newobj:
						newobj.append(m)
				flag=0
			else:
				if a not in newobj:
					newobj.append(a)
		i=i+1
		#print str(a)
		
	return newobj
while(1):
	inp=raw_input()
	inp=inp.lower()
	x=inp.split()
	print x
	x=clean(x)
	print x
	maxct=0
	for a in cluster:
		ct=0
		#print len(a)
		s='#'+a[0]
		if a[0] in x or s in x:
			index=a[0]
			break
		for y in x:
			#print y
			if y in a:
				ct=ct+1
			if y[1:] in a and y[0] =='#':
				ct=ct+2
		#print ct
		if ct> 0:
			print a[0]+str(ct)
		if ct>maxct:
			maxct=ct
			index=a[0]
		
	print index
	
