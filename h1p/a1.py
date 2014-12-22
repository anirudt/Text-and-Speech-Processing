'''
count() returns the emission estimate
'''

def count(x,y):
	L = open("gene.counts", "r").read().splitlines() #Split the lines of the count file
	I = open("gene.train","r").read() #Split the lines of the input data
	for line in L:
		if (line.count(x) and line.count(y)):
			if line[line.find(' ')+1:line.find(' ')+8]=="WORDTAG":
				a = int(line[0:line.find(' ')])
	return a*1.0/I.count(y)


'''
cls() returns the class a word belongs to
'''

def cls(x):
	y1 = "I-GENE"
	y2 = "O"
	v1 = count(x,y1)
	v2 = count(x,y2)
	s = v1 + v2
	v1 = v1/s
	v2 = v2/s
	if v1>0.5:
		print v1
		return y1
	else:
		print v2
		return y2

'''
tag_gen() finds the list of all tags present in the file
'''


def tag_gen():
	I = open("gene.train","r").read().splitlines()
	temp = []
	for line in I:
		temp.append(line[line.find(' ')+1:-1])
	temp=list(set(temp))
	return temp	
