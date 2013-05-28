import sys, re
import csv

def openFile(filename):
  return csv.reader(open(filename, "r"),delimiter='\t')

def writeTSV(analyzed_column,candidates):
	tsv_result=open("result.tsv","a")
	for candidate in candidates:
		tsv_result.write("C"+str(analyzed_column).zfill(3) +"\tC" + str(candidate.index).zfill(3)+"\n")
	tsv_result.close()
	
	
	
tsv_file = openFile(sys.argv[1])


class Candidate:
	def __init__(self, index):
		self.dependencies = {}
		self.index = index

	def test(self, key, row):
		value = row[self.index]
		if key in self.dependencies and self.dependencies[key] != value:
			False
		else:
			self.dependencies[key] = value
			True




for analyzed_column in range(800):
	candidates = [Candidate(i) for i in range(800) if i != analyzed_column]
	count = 0
	for row in tsv_file:
		count = count+1
		print ("Now on line" + str(count))
		key = row[analyzed_column]
		for candidate in candidates:
			if candidate.test(key, row):
				print ("Test successfull")
			else:
				print ("Test insuccessfull")
				print (key  + candidate.dependencies[key])
				candidates.remove(candidate)
		if len(candidates) == 0:
			break

		

	for candidate in candidates:
		print ("C"+str(analyzed_column).zfill(3) +"\tC" + str(candidate.index).zfill(3))
	writeTSV(analyzed_column,candidates)



