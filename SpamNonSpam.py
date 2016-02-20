'''Now given a mail, split it in terms of spaces,  and add up the log probability of each.  
   Multiply it with the spam probability. Do the same thing for non-spam.
   Whichever is higher  wins.
'''
import math
import os
import sys

def makeDict(f):
	temp = {}
	data = open(f,'r')
	for line in data:
		prob = line.split(" ")
		temp[prob[0]] = prob[1]
	return temp


def predict(basepath, f, dictionary):
	with open(os.path.join(basepath, f)) as toClassify:
		for line in toClassify:
			words = line.split(" ")
			spamP = 0
			nonspamP = 0
			for w in words:
				try:
					if w in dictionary:
						spamP = spamP + float(spamProbs[w].strip("\n"))
				except:
					pass
					
				try:
					if w in dictionary:
						nonspamP = nonspamP + float(nonspamProbs[w].strip("\n"))
				except:
					pass
					
		totalSpamP = spamP + math.log(0.5)
		totalnonSpamP = nonspamP + math.log(0.5)
		if(totalSpamP > totalnonSpamP):
			return True
		else:
			return False

spamProbs = makeDict(sys.argv[1]) #Pass the spam log probs here 
nonspamProbs = makeDict(sys.argv[2]) #Pass the non-spam log probs here
dictionaryWords = makeDict(sys.argv[5]) #Pass the dictionary 2500 words here
spamCount = 0
nonspamCount = 0

for f in os.listdir(sys.argv[3]):
	if predict(sys.argv[3], f, dictionaryWords):
		spamCount = spamCount + 1
	else:
		nonspamCount = nonspamCount + 1

spamCount = 0 
nonspamCount = 0

for f in os.listdir(sys.argv[4]):
	if predict(sys.argv[4], f, dictionaryWords):
		spamCount = spamCount + 1
	else:
		nonspamCount = nonspamCount + 1
		
print('Spam in {} is {} and non-spam is {}'.format(sys.argv[4], spamCount, nonspamCount))

