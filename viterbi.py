import re
import array
import string
import numpy as np
import math
import matplotlib.pyplot as plt
letter = []
for l in string.ascii_uppercase:
	letter.append (l)
letter.append(" ") 	#space between words

f_X= open ('initialstatedistribution.txt', 'r')
message_X = f_X.read()
f_X.close

#creating the pi matrix 27 * 1
for i in range(0,len(message_X)):
	x_values = message_X.split("\n")
#print(x_values)

ini = np.zeros(27)
for i in range(0, len(x_values)):
	ini[i] = float(x_values[i])
#print(ini)


f_Y= open ('transitionmatrix.txt', 'r')
message_Y = f_Y.read()
f_Y.close

#storing the aij matrix 27 * 27 P(St+1 = j|St=i)
aij= np.zeros([27,27])
for i in range(0, len(message_Y)):
	y_values = message_Y.split("\n")
for i in range(0,len(y_values)):
	y_value = y_values[i].split(" ")
	for j in range(0,27):
		aij[i][j] = float (y_value[j])
#print(aij)

f_Z= open ('hw7_emission.txt', 'r')
message_Z = f_Z.read()
f_Z.close

#storing the bik matrix 27*2 P(Ot=k|St=i)
bij = np.zeros([27,2])
for i in range(0, len(message_Z)):
	z_values = message_Z.split("\n");
for i in range(0, len(z_values)):
	z_value = z_values[i].split("\t")
	for j in range(0,2):
		bij[i][j] = float (z_value[j])
#print(bij)

f_O= open ('hw7_observations.txt', 'r')
message_O = f_O.read()
f_O.close

#storing the observations in an array
#obs_bin= np.zeros(325000)
obs_bin = []
regex_2 = r'(\d*)'
digit_list = re.findall(regex_2 , message_O)
digit = []
for i in digit_list:
  if i.isdigit() :
     int_i = int (i)
     obs_bin.append(int_i)
#print (obs_bin)
	
#computing the lij matrix[27*32500]
lij = np.zeros([27,325000])
lij.astype(float)
#print (lij)
max_index = []
#base case
max_term_s = -10000
index_i = 0
for i in range(0,27):
	lij[i][0] = math.log(ini[i] * bij[i][obs_bin[0]])			#choosing the index of b according to the observations
	if(lij[i][0] > max_term_s):
		max_term_s = lij[i][0]
		index_i = i
max_index.append(index_i)
print("kj")
print(max_index[0])
print ("jo")
print(letter[max_index[0]])
	
x_arr = []
y_arr = []
plt.subplot(2,1,1)
max_array =  np.zeros(27)
for t in range(1, 325000):
	index_i = 0
	for i in range(0,27):
		#computing tha array from where max is to be found
		for max_i in range(0,27):
			max_array[max_i]= lij[max_i][t-1] + math.log(aij[max_i][i])
		max_term = max(max_array)
		lij[i][t] = max_term + math.log(bij[i][obs_bin[t]])
		#print (lij[i][t])
print(lij)	
#backprop
max_index = np.zeros(325000)
max_index.astype(int)	
max_term_s = -100000000000000000000
for i in range(0,27):
	if (lij[i][324999] > max_term_s):
		max_term_s = lij[i][t]
		index_i = i
max_index[324999] = index_i

max_array = np.zeros(27)
for t_range in range(0,324998):
	t = 324998 - t_range
	print(type(max_index[324999]))
	for i in range(0,27):
		index = max_index[t+1]
		print(math.log(aij[i][index]))
		max_array[i] = lij[i][t-1] + math.log(aij[i][index])
	max_term = max(max_array)
	for a in range(0,27):
		if(max_array[a] == max_term):
			max_index[t] = a

print (max_index)	
for t in range(0,325000):
	plt.plot(t, max_index)

plt.show()










	
	
	



	
			

			
	

	
	
	
