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
		if a =='n' or a in stopwords:
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
