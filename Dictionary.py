#This script reads all files in all directories of the folder taken from the openClassroom site and generates the dictionary, which we can then store in a file 

from collections import defaultdict
from collections import OrderedDict
import os
import operator
import sys


dictionary = defaultdict(int)



for root, dirnames, filenames in os.walk(sys.argv[1]):
	for d in dirnames:
		for f in os.listdir(os.path.join(root, d)):
			with open(os.path.join(sys.argv[1], d, f)) as data:
				for line in data:
					words = line.split()
					for w in words:
						dictionary[w] += 1
	dictionary = OrderedDict(sorted(dictionary.items(),key = lambda t: t[1]))
with open(sys.argv[2], 'w') as fdict:
	for k in dictionary:
		fdict.write("{} {} \n".format(k, str(dictionary[k])))

	

