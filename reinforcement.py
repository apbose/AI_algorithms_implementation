import array
import string
import numpy as np
from numpy.linalg import inv
import math
import matplotlib.pyplot as plt

discount_factor = 0.99

#reading the rewards of the states
f_rewards = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_rewards.txt', 'r')
f_rewards_state_read = f_rewards.read()
f_rewards_states = f_rewards_state_read.split("\n")
#print (f_rewards_states[70])
f_rewards.close() 

f_rewards_int = map(lambda x: int(x), f_rewards_states)
#print(list(f_rewards_int))
reward_int = list(f_rewards_int)
reward_mat = np.zeros([81,1])
for i in range(0,81):
	reward_mat[i][0] = reward_int[i]

##west - ac1
##north -ac2
##east - ac3
##south - ac4

f_state_ac1 = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_transition_ac1.txt', 'r')
f_state_ac1_read = f_state_ac1.read()
f_state_ac1_arr = f_state_ac1_read.split("\n")
#print(f_state_ac1_arr)
f_state_ac1.close() 


f_state_ac1_mat = np.zeros([400,3])
for i in range(0,len(f_state_ac1_arr)):
	#print(f_state_ac1_arr[i])
	f_state_ac1_mat_new = f_state_ac1_arr[i].split()
	#print(len(f_state_ac1_mat_new))
	for j in range(0, 3): #should be 3
		#print(j)
		f_state_ac1_mat[i][j] = float(f_state_ac1_mat_new[j])
#print (f_state_ac1_mat)

f_state_ac1 = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_transition_ac1.txt', 'r')
f_state_ac1_read = f_state_ac1.read()
f_state_ac1_arr = f_state_ac1_read.split("\n")
#print(f_state_ac1_arr)
f_state_ac1.close() 


f_state_ac1_mat = np.zeros([400,3])
for i in range(0,len(f_state_ac1_arr)):
	#print(f_state_ac1_arr[i])
	f_state_ac1_mat_new = f_state_ac1_arr[i].split()
	#print(len(f_state_ac1_mat_new))
	for j in range(0, 3): #should be 3
		f_state_ac1_mat[i][j] = float(f_state_ac1_mat_new[j])
#print (f_state_ac1_mat)

f_state_ac2 = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_transition_ac2.txt', 'r')
f_state_ac2_read = f_state_ac2.read()
f_state_ac2_arr = f_state_ac2_read.split("\n")
#print(f_state_ac1_arr)
f_state_ac2.close() 

f_state_ac2_mat = np.zeros([400,3])
for i in range(0,len(f_state_ac2_arr)):
	#print(f_state_ac1_arr[i])
	f_state_ac2_mat_new = f_state_ac2_arr[i].split()
	#print(len(f_state_ac1_mat_new))
	for j in range(0, 3): #should be 3
		f_state_ac2_mat[i][j] = float(f_state_ac2_mat_new[j])
#print (f_state_ac2_mat)

f_state_ac3 = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_transition_ac3.txt', 'r')
f_state_ac3_read = f_state_ac3.read()
f_state_ac3_arr = f_state_ac3_read.split("\n")
#print(f_state_ac1_arr)
f_state_ac3.close() 

f_state_ac3_mat = np.zeros([400,3])
for i in range(0,len(f_state_ac3_arr)):
	#print(f_state_ac1_arr[i])
	f_state_ac3_mat_new = f_state_ac3_arr[i].split()
	#print(len(f_state_ac1_mat_new))
	for j in range(0, 3): #should be 3
		f_state_ac3_mat[i][j] = float(f_state_ac3_mat_new[j])
#print (f_state_ac3_mat)

f_state_ac4 = open ('C:/Users/apurb/Documents/ucsd_studies/quarter_1/cse_250a/hw/hw9/hw9_transition_ac4.txt', 'r')
f_state_ac4_read = f_state_ac4.read()
f_state_ac4_arr = f_state_ac4_read.split("\n")
#print(f_state_ac1_arr)
f_state_ac4.close() 

f_state_ac4_mat = np.zeros([400,3])
for i in range(0,len(f_state_ac4_arr)):
	#print(f_state_ac1_arr[i])
	f_state_ac4_mat_new = f_state_ac4_arr[i].split()
	#print(len(f_state_ac1_mat_new))
	for j in range(0, 3): #should be 3
		f_state_ac4_mat[i][j] = float(f_state_ac4_mat_new[j])
#print (f_state_ac4_mat)

#computing the transition matrix, s is rows S' is column
trans_west_mat= np.zeros([81,81])
#print(trans_west_mat)
#trans_west_mat= np.matrix(trans_west_mat)
for i in range(0,len(f_state_ac1_arr)):
	s_index = int (f_state_ac1_mat[i][0])-1
	s_bar_index = int (f_state_ac1_mat[i][1])-1
	trans_west_mat[s_index][s_bar_index] = f_state_ac1_mat[i][2]


trans_north_mat= np.zeros([81,81])
for i in range(0,len(f_state_ac2_arr)):
	s_index = int (f_state_ac2_mat[i][0]) -1
	s_bar_index = int (f_state_ac2_mat[i][1]) -1
	trans_north_mat[s_index][s_bar_index] = f_state_ac2_mat[i][2]
	
trans_east_mat= np.zeros([81,81])
for i in range(0,len(f_state_ac3_arr)):
	s_index = int (f_state_ac3_mat[i][0])
	s_bar_index = int (f_state_ac3_mat[i][1])
	trans_east_mat[s_index - 1][s_bar_index - 1] = f_state_ac3_mat[i][2]

trans_south_mat= np.zeros([81,81])
for i in range(0,len(f_state_ac4_arr)):
	s_index = int (f_state_ac4_mat[i][0])
	s_bar_index = int (f_state_ac4_mat[i][1])
	trans_south_mat[s_index - 1][s_bar_index - 1] = f_state_ac4_mat[i][2]

trans_west_mat= np.matrix(trans_west_mat)
trans_east_mat= np.matrix(trans_east_mat)
trans_south_mat= np.matrix(trans_south_mat)
trans_north_mat= np.matrix(trans_north_mat)

identity_mat = np.matrix(np.identity(81))
def compute_value_state_mat(current_policy):
	p_mat = np.zeros([81,81])
	for state in range(0,81):
		#meaning that the policy comes out to be going west
		if(current_policy[state] == 0):
			p_mat[state][:] = trans_west_mat[state][:]
		#meaning that the policy comes out to be going north
		if(current_policy[state] == 1):
			p_mat[state][:] = trans_north_mat[state][:]
		#meaning that the policy comes out to be going east
		if(current_policy[state] == 2):
			p_mat[state][:] = trans_east_mat[state][:]
		#meaning that the policy comes out to be going south
		if(current_policy[state] == 3):
			p_mat[state][:] = trans_south_mat[state][:]
	#initially taking all the value as west
	value_state_mat = np.matmul((np.linalg.inv(identity_mat - discount_factor*p_mat)), reward_mat)  #81*81 * 81*1 = 81 *1 for each state
	#print(value_state_mat)
	return value_state_mat

Q_val = np.zeros(4)
policy_iter = np.zeros([81,1])
#policy_iter = np.matrix(policy_iter)
def compute_new_policy(value_state_mat):
	for state in range(0,81):
		max = -100000;
		max_till = -1
		p1 = np.matmul(trans_west_mat[state][:], value_state_mat)        #1*81 * 81*1
		if(p1 > max):
			max =p1
			max_till = 0
			
		p2 = np.matmul(trans_north_mat[state][:], value_state_mat)        #1*81 * 81*1
		if(p2 > max):
			max =p2
			max_till = 1
		
		p3 = np.matmul(trans_east_mat[state][:], value_state_mat)        #1*81 * 81*1
		if(p3 > max):
			max =p3
			max_till = 2
		
		p4 = np.matmul(trans_south_mat[state][:], value_state_mat)        #1*81 * 81*1
		if(p4 > max):
			max =p4
			max_till = 3
		#print (state);
		policy_iter[state][0] = max_till
	#print (policy_iter)
	return policy_iter

current_policy = np.zeros([81,1])	#initialiing all to west
#######################################policy iteration######################################
for iter in range(0,100):
	value_state_mat_iter = compute_value_state_mat(current_policy)  #81*1
	current_policy = compute_new_policy(value_state_mat_iter)    #81 denoting the actiob for each state

print (value_state_mat_iter)
for i in range(0,81):
	if(current_policy[i] == 0):
		print (i+1, "state -> west")
	if(current_policy[i] == 1):
		print (i+1, "state -> north")
	if(current_policy[i] == 2):
		print (i+1, "state -> east")	
	if(current_policy[i] == 3):
		print (i+1, "state -> south")	
		
#print(reward_mat)
	
#########################################value iteration##################################3

value_state_mat_init= np.zeros([81,1])
value_state_mat= np.zeros([81,1])
for i in range(0,5000):
	for state in range(0,81):
		max_val = -10000
		max_till = -1
		p1 = np.matmul(trans_west_mat[state][:], value_state_mat_init)
		if(p1 > max_val):
			max_val =p1
		p2 = np.matmul(trans_north_mat[state][:], value_state_mat_init)
		if(p2 > max_val):
			max_val =p2
		p3 = np.matmul(trans_east_mat[state][:], value_state_mat_init)
		if(p3 > max_val):
			max_val =p3
		p4 = np.matmul(trans_south_mat[state][:], value_state_mat_init)
		if(p4 > max_val):
			max_val =p4	
		value_state_mat[state][0] = reward_mat[state][0] + discount_factor * (max_val)
	value_state_mat_init = value_state_mat

#print(value_state_mat_init)





