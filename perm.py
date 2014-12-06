from itertools import permutations
from random import shuffle
import enchant
def shuffled_perm(s,num):
	perms = list(permutations(s, num))
	
	shuffle(perms)
	res = []
	i = []
	a = ""
	print "Stage 1"
	for e in perms:
		a = ""
		for s in e:
			a = a + s
		i.append(a)	
	print "Stage interim"	
	d = enchant.Dict("en_us")
	for e in i:
		if d.check(e):
#			print "Stage 2"
			res.append(e)
	print "Stage 2"
	return ["".join(p) for p in res] # rebuild strings and return

def main():
	string = "PYERTCOAESOFOS"
	num = 6
	tot_num = 14
	l = []
	print shuffled_perm(string, num)


