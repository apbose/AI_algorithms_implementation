import re
import array
import string
import numpy as np
import math

f_X= open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw8/movie_title.txt', 'r')
message_X = f_X.read()
f_X.close()

f_Y= open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw8/hw8_rating.txt', 'r')
message_Y = f_Y.read()
f_Y.close()

def find_key(val, dict_to_search):
	for k,v in dict_to_search.items():
		if v == val :
			return k

for i in range(0,len(message_X)):
	movie_titles = message_X.split("\n")

rating_matrix= np.chararray([500,62])
samples = 0
for i in range(0,len(message_Y)):
	movie_rating = message_Y.split("\n")
	samples = len(movie_rating)
	for j in range (0, len(movie_rating)):
		rating_matrix[j] = movie_rating[j].split(" ")
#print (rating_matrix[264])

print(samples)
count_mean = {}  #hash according to movie

for j, movie in enumerate(movie_titles):
	count_approved = 0;
	count = 0;
	for i in range (0, samples):
		if(rating_matrix[i][j] != b'?'):
			count = count + 1;
			if(rating_matrix[i][j] == b'1'):   #meaning movie j is approved
				count_approved = count_approved + 1;
			
	count_mean[movie] = count_approved/count

print(count_mean)

count_mean_value = map(lambda x: count_mean[x], movie_titles)
mean_val = list(count_mean_value);
mean_val.sort()
print(mean_val)

#A part: print the movie preferences
movie_order = map(lambda x: find_key(x, count_mean), mean_val)
print(list(movie_order))

#e part:compute the e step
f_Z= open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw8/hw8_probz.txt', 'r')
message_Z = f_Z.read()
f_Z.close()

f_R_givenZ = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw8/hw8_probRgiven Z.txt', 'r')
message_R_givenZ = f_R_givenZ.read()
movie_given_Z = message_R_givenZ.split("\n")
f_R_givenZ.close()

#storing the R given Z in a 62*4 matrix
R_givenZ = np.zeros([62,4])
for i in range(0,len(movie_given_Z)):
	R_givenZ_new = movie_given_Z[i].split("  ")
	for j in range (0, len(R_givenZ_new)):
		R_givenZ[i][j]= float(R_givenZ_new[j])
print(R_givenZ)


for i in range(0,len(message_Z)):
	prob_z = (message_Z.split("\n"))
#print(prob_z)

prob_z_float = np.zeros(4)
for i in range(0,len(prob_z)):
	prob_z_float[i] = float(prob_z[i])
#print(prob_z_float)

prob_z_flt = np.zeros([128,4])
sum_denom = np.zeros(128)  # will contain the denominators
pho_t = np.zeros(269) #for each student
for i in range(0,128):   	#i denotes iteration
	
	for j in range(0,4):	#j denotes z
		
		sum_pho = 0
		for t in range(0, samples):   #iterating over students
			if(i != 0):
				numerator = prob_z_flt[i-1][j] #(P(Z=i) term) for each student  which needs to be reset
			if(i == 0):
				numerator = 0.25
			sum_denom = 0
			for iter_i in range(0,4):
				if(i != 0):
					prod_denom = prob_z_flt[i-1][iter_i] #(P(Z=i) term)
				if(i == 0):
					prod_denom = 0.25
				for m in range(0,62):   #iterating over movies
					if(rating_matrix[t][m] == b'1' or rating_matrix[t][m] == b'0'):  #visible nodes
						if(rating_matrix[t][m] == b'1'):
							prod_denom = prod_denom *  R_givenZ[m][iter_i]
						else:
							prod_denom = prod_denom * (1 - R_givenZ[m][iter_i])
				#print ("proddenom")
				#print (prod_denom)
				#print("student, k, iteration")
				#print(t , iter_i, i)
				#print(prod_denom)
				sum_denom = sum_denom + prod_denom #this is for all four k's at a particular student
				
				
			#print("Z=j, iteration, numerator")
			#print(j, i,numerator)
			for m in range(0,62):   #iterating over movies for a particular student and particular Z =j
				if(rating_matrix[t][m] == b'1' or rating_matrix[t][m] == b'0'):  #visible nodes
					if(rating_matrix[t][m] == b'1'):
						numerator = numerator *  R_givenZ[m][j]
					else:
						numerator = numerator * (1 - R_givenZ[m][j])
			#print("student, Z=j, iteration, denominator, numerator")
			#print(t, j, i, sum_denom,numerator)
			#print("prodnum, Z=j")	
			#print(numerator,j)
			pho_t[t] = numerator/sum_denom # for a particular i and Z
			print(sum_pho, j, samples, t)
			sum_pho = sum_pho + pho_t[t]
		#print(sum_pho)
		prob_z_flt[i][j] = sum_pho/269
		
		#now finding for each movie m given Z=i and iteration in the outer loop
		#for m in range(0,62):

		for m in range(0,62):
			sum_m_seen = 0 #common for all t's
			sum_m_not_seen = 0
			for t in range(0,samples):
				if(rating_matrix[t][m] == b'1' or rating_matrix[t][m] == b'0'): #visible nodes
					if(rating_matrix[t][m] == b'1'):
						sum_m_seen = sum_m_seen + pho_t[t]
				if(rating_matrix[t][m] == b'?'):# m falls in invisible node
					sum_m_not_seen = sum_m_not_seen + (pho_t[t] * R_givenZ[m][j])
				
				
			R_givenZ[m][j] = (sum_m_seen + sum_m_not_seen)/sum_pho    #updates for each m
	print(prob_z_flt[i])
	log_prob = 0
	for t in range(0,samples):
		sum_iter = 0
		for iter_i in range(0,4):
			prod_likeli = prob_z_flt[i][iter_i]
			for m in range(0,62):
				if(rating_matrix[t][m] == b'1' or rating_matrix[t][m] == b'0'):  #visible nodes
					if(rating_matrix[t][m] == b'1'):
						prod_likeli = prod_likeli *  R_givenZ[m][iter_i]
					else:
						prod_likeli = prod_likeli * (1 - R_givenZ[m][iter_i])
			sum_iter = sum_iter + prod_likeli  #will take the sum over all 4 k'sfor particular t
			#print (iter_i,sum_iter)
		log_prob = log_prob + (math.log(sum_iter))
	print ("iteration no");
	print (i)
	print (log_prob/270)
		
		
		
			
		