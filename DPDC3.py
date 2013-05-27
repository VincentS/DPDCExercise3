import sys, re
import csv

tsv_file = openFile(sys.argv[1])
analyzed_column = int(sys.argv[2])

class Candidate:
	def __init__(self, index):
		self.dependencies = {}
		self.index = index

	def test(self, key, row):
		value = row[self.index]
		if key in self.dependencies:
			self.dependencies[key] == value
		else:
			self.dependencies[key] = value
			True

candidates = [Candidate(i) for i in range(800) if i != analyzed_column]

def openFile(filename):
	return csv.reader(open(filename, "rb"),delimiter='\t')

count = 0
for row in tsv_file:
	count = count+1
	print "Now on line" + str(count)
	key = row[analyzed_column]
	for candidate in candidates:
		if candidate.test(key, row):
			print "Test successfull"
		else:
			print "Test insuccessfull"
			candidates.remove(candidate)
	if len(candidates) == 0:
		break

for candidate in candidates:
	print "C"+str(analyzed_column) +"--> C" + str(candidate.index)
