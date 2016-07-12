'''
1)cleaning every word from tweet 
2)input=list of words,op: list of cleaned words
'''
__author__ = 'ankit'

from classes import stopwords
def clean(parliament):
	redundant=[':',",",")",".","(",";","/","|","-",'?','=','+']
	i=0
	flag=0
	newobj=[]
	m=0
	#print parliament
	for a in parliament:
		
		#print str(i)+'  '+str(a)
		a=a.lower()
		if "http" in a or "\xe2\x80\xa6" in a:
			continue	
		while a[-1] in redundant:
			if len(a)>1:
				a=a[:-1]		
			else:
				a="n"

		
		while a[0] in redundant:
			if len(a)>1:
				a=a[1:]
			else:
				a="n"
		
		if ',' in a:
			b=a.split(',')
			flag=1
		
		if a =='n' or a in stopwords :
			m=1
		
		else:
		
			if flag==1:
				for m in b:
					if m not in newobj:
						newobj.append(m)
				flag=0
			else:
				if a not in newobj:
					newobj.append(a)
		
		#print str(a)
		
		i=i+1
		
	return newobj

	
#clean(['#transformingindia.', 'in', 'defence', 'india', 'is', 'most', 'powerful', 'than', 'ever', 'before.', 'proud', 'of', 'pm.'])
