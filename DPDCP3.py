import sys, re
import csv

def openFile(filename):
	return csv.reader(open(filename, "r"),delimiter='\t')

def writeTSV(analyzed_column,candidates):
	tsv_result=open("result.tsv","a")
	for candidate in candidates:
		tsv_result.write("C"+str(analyzed_column).zfill(3) +"\tC" + str(candidate.index).zfill(3)+"\n")
	tsv_result.close()





class Candidate:
	def __init__(self, index):
		self.dependencies = {}
		self.index = index

	def test(self, key, row):
		value = row[self.index]
		if key in self.dependencies:
			return self.dependencies[key] == value
		else:
			self.dependencies[key] = value
			return True

for analyzed_column in range(800):
	candidates = [Candidate(i) for i in range(800) if i != analyzed_column]
	row_id = 0
	tsv_file = openFile(sys.argv[1])
	for row in tsv_file:
		key = row[analyzed_column]
		for candidate in candidates:
			if not candidate.test(key, row):
				candidates.remove(candidate)
		if len(candidates) == 0 or row_id > 5000:
			break
		row_id += 1


	for candidate in candidates:
		print ("C"+str(analyzed_column).zfill(3) +"\tC" + str(candidate.index).zfill(3))
	writeTSV(analyzed_column,candidates)



