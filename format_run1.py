import sys
import glob
import math
import operator

from collections import defaultdict

qrel_file = 'QRELS'
qrel_res = defaultdict(list)

rel_docs = {}
retrieved_rel_docs = {}

with open(qrel_file) as f:
	content = f.read().splitlines()
	for line in content:
		l = line.split(" ")
		#qrel_res[l[0]].append(l[2])
		rel_docs[l[0]] = 0
		if(int(l[3]) == 1):
			qrel_res[l[0]].append(l[2])
			rel_docs[l[0]]=rel_docs[l[0]]+1;

qpath = 'queries/test/*'
qfiles = glob.glob(qpath)

rpath = 'responses/*'
for qfile in qfiles:
	qname = qfile[len(qfile)-4:len(qfile)]
	query = []
	with open(qfile) as qf:
		qr = qf.read().splitlines()
		for line in qr:
			qt = int(line.split(",")[0])
			query.append(qt)


	files = glob.glob(rpath)

	scores = {}
	for response_file in files:
		response = []
		with open(response_file) as f:
			r = f.read().splitlines()
			for line in r:
				response_term = int(line.split(",")[0])
				response.append(response_term)

		#Calculate score for this response
		score = 0
		for qterm in query:
			min_difference = 10000000000000
			for rterm in response:

				
				difference = math.sqrt(((qterm) - (rterm))**2)
				
				if(difference < min_difference):
					min_difference = difference
			score = score+min_difference
		scores[response_file] = score/len(query)
	sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))

	for i in range(0,1000):
		qres = sorted_scores[i][0][len(sorted_scores[i][0])-4:len(sorted_scores[i][0])];

		print (qname)+" Q0 "+ str(qres) + " 1"