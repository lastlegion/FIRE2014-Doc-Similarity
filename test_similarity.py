import sys
import glob
import math
import operator

from collections import defaultdict

qrel_file = 'QRELS'
qrel_res = defaultdict(list)
with open(qrel_file) as f:
	content = f.read().splitlines()
	#print content
	for line in content:
		l = line.split(" ")
		#qrel_res[l[0]].append(l[2])
		if(int(l[3]) == 1):
			qrel_res[l[0]].append(l[2])
print qrel_res	

qpath = 'queries/train/*'
qfiles = glob.glob(qpath)

rpath = 'responses/*'
for qfile in qfiles:
	qname = qfile[len(qfile)-4:len(qfile)]
	print qname
	query = []
	with open(qfile) as qf:
		qr = qf.read().splitlines()
		for line in qr:
			qt = int(line.split(",")[0])
			query.append(qt)

	'''
	with open("queries/train/Q001") as f:
		content = f.read().splitlines()

	query = []

	#Extract psuedo terms from query
	for line in content:
		term = line.split(",")[0]*1;
		query.append(int(term))
	'''

	files = glob.glob(rpath)

	scores = {}
	for response_file in files:
		#print response_file
		response = []
		#Fill response list
		with open(response_file) as f:
			r = f.read().splitlines()
			for line in r:
				response_term = int(line.split(",")[0])
				response.append(response_term)

		#Calculate score for this response
		score = 0
		for qterm in query:
			#min_difference = 10000000000000
			for rterm in response:

				
				difference = math.sqrt(((qterm) - (rterm))**2)
				
				#if(difference < min_difference):
					#min_difference = difference
			score = score+difference
		scores[response_file] = score
	sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))

	for i in range(0,1000):
		qres = sorted_scores[i][0][len(sorted_scores[i][0])-4:len(sorted_scores[i][0])];
		#print qrel_res[qname]
		for res_f in qrel_res[qname]:
			if(qres == res_f):
				print qres
	
	print "---"

	#Compare results with QRELS

	#for res_f in qrel_res[qname]:
	#	if(res_f)


'''
for response in files:
	response_doc = []
	with open(response) as f:
		r = f.read().splitlines()
		for line in r:
			t = line.split(",")[0]*1;
			response_doc.append(t)
	print response_doc
	
	qscore = 0
	for qterm in query:
		min_difference = 10000000
		#For every query term find corresponding minimum doc term
		for rterm in response_doc:
			difference = (int(qterm) - int(rterm))**2
			if(difference < min_difference ):
				min_difference = difference
				#min_doc = doc
		qscore += min_difference

	print qscore
'''