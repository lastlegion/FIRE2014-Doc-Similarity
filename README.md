FIRE2014-Doc-Similarity
=======================

The Task description:
=======================
This work is a part of our participation in the "Document Similarity Amid Automatically Detected Terms" task of FIRE 2014.
Given a set of queries and a set of responses, both represented as sets of such segments, the purpose of this task is to identify response documents that are related to each query.

Corpus:
=======================
There are a total 3,148 documents, consisting of 149 queries and 2,999 responses. The entire collection of responses will be available to participants. Queries are divided into test and training sets. The training set consists of 16 queries, along with relevance judgements for those queries. The testing phase will consists of some subset of the remaining 133 queries. 

Documents, specifically, are CSV files with three columns: psuedo-term, start time, and end time. Psuedo-terms are regions of speech that appear throughout the corpus. Other documents may have similar psuedo-terms if regions were deemed to be similar in the audio space. The start and end regions mark where a given term appeared within an audio file. While psuedo-term itself is not necessarily unique, the (psuedo-term,start,end) generally is. To obtain the data, participants must register with the organisers.

Evaluation:
=======================
Participating systems are asked to submit results to depth-1000. Evaluators will then create binary relevance judgements across depth-10 pooling; deeper pooling will be considered if resources allow. The principal evaluation measure will be mean average precision (MAP).

