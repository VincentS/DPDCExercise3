import sys, re
import csv

class columnDict(object):
	dict={}

candidates=range(800)
del candidates[int(sys.argv[2])]
instancelist = [ columnDict() for i in range(800)]

def openFile(filename):
	return csv.reader(open(filename, "rb"),delimiter='\t')

def main():
	count = 0

	tsv_file = openFile(sys.argv[1])
	for row in tsv_file:
		count = count+1
		print "Now on line" + str(count)	
	
		for j in candidates:
			if row[int(sys.argv[2])] not in instancelist[j].dict:
				instancelist[j].dict[row[int(sys.argv[2])]]=row[j]
				print "Test"
			elif instancelist[j].dict.get(row[int(sys.argv[2])])!=row[j]:
				del candidates[j]
				print "Delete"
				
	
				
	for s in candidates:
		print "C"+sys.argv[2] +"--> C" + s
	
if __name__ == '__main__':
   main()