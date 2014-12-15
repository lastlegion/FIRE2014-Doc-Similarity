import sys
import glob
import math
import operator
import numpy as np

from collections import defaultdict

qrel_file = 'QRELS'
qrel_res = defaultdict(list)

rel_docs = {}
retrieved_rel_docs = {}

n_retrieved=0

with open(qrel_file) as f:
	content = f.read().splitlines()
	for line in content:
		l = line.split(" ")
		rel_docs[l[0]] = 0
		if(int(l[3]) == 1):
			qrel_res[l[0]].append(l[2])
			rel_docs[l[0]]=rel_docs[l[0]]+1
qpath = 'queries/test/*'
qfiles = glob.glob(qpath)
num_rel = 0

rpath = 'responses/*'
for qfile in qfiles:
	qname = qfile[len(qfile)-4:len(qfile)]
	query = []
	query_arr = np.array([])
	with open(qfile) as qf:
		qr = qf.read().splitlines()
		for line in qr:
			q_param_1 = int(line.split(",")[0])
			beg = int(line.split(",")[1])
			end = int(line.split(",")[2])
			q_param_2 = end-beg
			query.append([q_param_1, q_param_2])

	files = glob.glob(rpath)
	scores = {}
	#print query
	for response_file in files:
		#		print response_file

		response = []
		response_arr = np.array([])
		with open(response_file) as f:
			r = f.read().splitlines()
			for line in r:
				response_param_1 = int(line.split(",")[0])
				beg = int(line.split(",")[1])
				end = int(line.split(",")[2])
				response_param_2 = end-beg
				response.append([response_param_1, response_param_2])
		#response_arr.append(np.array(responses))
		#calculate scores for this response
		score = 0
		#print response
		for qterm in query:
			min_difference = 100000000000000
			for rterm in response:
				difference = math.sqrt((qterm[1] - rterm[1])**2)
				if(difference < min_difference):
					min_difference = difference
				#print min_difference
			score = score+min_difference
		scores[response_file]=  score#/len(query)
	sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))

	R=0
	#print "done"
	for i in range(0,1000):
		qres = sorted_scores[i][0][len(sorted_scores[i][0])-4:len(sorted_scores[i][0])]
		print (qname)+" Q0 "+ str(qres) + " 1"
		'''
		for rel_doc in qrel_res[qname]:
			if int(qres) == int(rel_doc):
				num_rel = num_rel+1
				#print num_rel
		'''
	#print num_rel
