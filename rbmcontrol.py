  
#follows 3.1 from https://arxiv.org/pdf/1402.6238.pdf

#first associates list of topic distributions from LDA output with the movieID in topicdist (uses mallet.csv as input)
#then opens all user ratings (ratings.csv), finds sum (userRatingsSum) to normalize them later
#replaces all instances of movieIDS from user ratings with that particular movie's topic distribution from topicdist
#normalizes the ratings and then multiplies values from topicdist by their new normalized rating
#use dict to match each of the 100 topics that are given distributions by LDA with what the topics in English mean and pair with user rating for each
#create all user profiles by summing ratings for all movies (100 values overall, one for each of 100 topics output by LDA)
#call function to produce a certain user's user profile

#big question:
#lastly, how do we actually output a set of movie recommendations based on the topics they rated highly

import csv
import sys
from csv import reader
from collections import defaultdict
import pandas as pd 
import numpy as np
import numpy.ma as ma
# from itertools import zip_longest
import pickle
import scipy.stats as sc
import math

# #associate them w their movieIDs in a big dict
# topicdist= defaultdict(list)
# with open('mallet.csv', 'r') as read_obj:
# 	# pass the file object to reader() to get the reader object
# 	csv_reader = reader(read_obj)
# 	# Pass reader object to list() to get a list of lists
# 	list_of_rows = list(csv_reader)

# #make list of topicdists for each movie
# for row in list_of_rows:
# 	for x in row[2:]:
# 		topicdist[row[1]].append(x)
		
# #opens ratings for all 
# reader = csv.DictReader(open('ratings.csv','r'))
# dict_list = []
# #finding sum rating for each user for later use
# usersRatingsSum = defaultdict(int)
# for line in reader:
# 	dict_list.append(line)
# 	usersRatingsSum[line['user_id']] += (int(line['rating']))

# #replace all w topic distribution from mallet
# for x in dict_list:
# 	x['movie_id'] = topicdist.get(x.get('movie_id'))

# #normalize ratings based on sum
# #multiply by value
# for x in dict_list:
# 	x['rating'] = float(x['rating'])/float(usersRatingsSum.get(x.get('user_id')))
# 	if x['movie_id'] is not None:
# 		for val in x['movie_id']:
# 			val = float(val) * float(x['rating'])

# # print(dict_list)

# #convert back to topics by ordering from csv (made txt from mallet output to parse easier), store in dict
# f = open('topic-keys.txt','r')
# out = f.readlines() 
# topicKeys = defaultdict(list)
# counter = 0
# for x in out:
# 	topicKeys[counter] = x.rstrip('\n')
# 	counter += 1

# #creates all user profiles
# def save_user_profiles():
# 	allUsers = defaultdict(list)
# 	for users in range(6040):
# 		tmp_listforusr = []
# 		for reviews in dict_list:
# 			if reviews['user_id'] == str(users):
# 				if reviews['movie_id']:
# 					#have to convert str to floats
# 					floats = list(map(float, reviews['movie_id']))
# 					tmp_listforusr.append(floats)
# 		sums = np.sum(tmp_listforusr, axis=0)
# 		allUsers[users] = (sums)
# 	print(allUsers)

# 	with open('user_profiles.p', 'wb') as fp:
# 		pickle.dump(allUsers, fp, protocol=pickle.HIGHEST_PROTOCOL)


# # gets particular user's profile
# def getUserProfile(id):
# 	userdict = {}
# 	counter = 0
# 	currList = allUsers.get(id)
# 	for rating in currList:
# 		userdict[topicKeys[counter]] = rating
# 		counter += 1
# 	print(userdict)

# save_user_profiles()
# getUserProfile(1)




#takes specific userID # to generate recommendations for
# user_of_interest = int(sys.argv[1])
# num_of_recs = int(sys.argv[2])
# size_of_neighborhood = int(sys.argv[3])
num_of_recs = 100
size_of_neighborhood = 100

allUsers = {}
with open('user_profiles.p', 'rb') as fp:
	allUsers = pickle.load(fp)

# print(len(allUsers.keys()))

# takes in latent topic vectors
def topic_similarity(u1, u2):
	# print(u1.shape)
	# print(u2.shape)
	entropy = sc.entropy(u1, u2)
	return math.exp(entropy)

# takes in user ratings vectors and calculates pearson correlation similarity
def rating_similarity(object1, object2):
    values = range(len(object1))
    
    # Summation over all attributes for both objects
    sum_object1 = sum([float(object1[i]) for i in values]) 
    sum_object2 = sum([float(object2[i]) for i in values])

    # Sum the squares
    square_sum1 = sum([pow(object1[i],2) for i in values])
    square_sum2 = sum([pow(object2[i],2) for i in values])

    # Add up the products
    product = sum([object1[i]*object2[i] for i in values])

    #Calculate Pearson Correlation score
    numerator = product - (sum_object1*sum_object2/len(object1))
    denominator = ((square_sum1 - pow(sum_object1,2)/len(object1)) * (square_sum2 - 
    	pow(sum_object2,2)/len(object1))) ** 0.5
        
    # Can"t have division by 0
    if denominator == 0:
        return 0

    result = numerator/denominator
    return result


def load_ratings_matrix():
	path = 'ratings.csv'
	ratings_df = pd.read_csv(path)
	ratings_mat = np.zeros((6041, 3953), dtype=int)
	for index, row in ratings_df.iterrows():
		ratings_mat[row['user_id'], row['movie_id']] = row['rating']
	np.savetxt('ratings_mat.csv', ratings_mat, delimiter=',')
	return ratings_mat

ratings_mat = load_ratings_matrix()

# stores ratings_mat so won't have to recalculate each time
# ratings_mat = np.loadtxt(open("ratings_mat.csv", "rb"), delimiter=",")

def build_sim_matrix(user_mat, ratings_mat, n_users=size_of_neighborhood):
	sim_mat = np.zeros((n_users, n_users), dtype=float)
	for i in range(1, n_users, 1):
		print(i)
		for j in range(i, n_users, 1):
			# print(i,j)
			topic_sim = topic_similarity(allUsers[i], allUsers[j])
			rating_sim = rating_similarity(ratings_mat[i], ratings_mat[j])
			sim_mat[i, j] = topic_sim * rating_sim
	np.savetxt('similarity_mat1.csv', sim_mat, delimiter=',')
	return sim_mat

sim_mat = build_sim_matrix(allUsers, ratings_mat, n_users=size_of_neighborhood)
sim_mat = np.loadtxt(open("similarity_mat1.csv", "rb"), delimiter=",")
print("DONE BUILDING SIM MATRIX")

def get_neighborhood(user, sim_mat, n):
	users_sorted = sorted(range(len(sim_mat[user])), key=lambda j: sim_mat[min(user,j), max(user,j)], reverse=True)
	n = min(n, len(users_sorted))
	return users_sorted[:n]

def get_recommendations(user, sim_mat, ratings_mat, k, n, threshold_rating=3):
	neighborhood = get_neighborhood(user, sim_mat, n)

	# get all L items
	L = {}
	for i in neighborhood:
		# print('NEIGHBOR: ', i)
		for item in range(len(ratings_mat[i])):
			if ratings_mat[i, item] >= threshold_rating:
				L[item] = L.get(item, 0) + 1
	sorted_L = {k: v for k, v in sorted(L.items(), key=lambda item: item[1], reverse=True)}
	# print(sorted_L)
	# print("SORTED_L: ",len(sorted_L))
	for i in range(len(ratings_mat[user])):
		if ratings_mat[user, i] != 0.0:
			sorted_L.pop(i, None)
			# print(popped)

	min_k = min(k, len(sorted_L.keys()))
	tmp = list(sorted_L.keys())[:min_k]
	return list(map(str, tmp))

#ouputs recommendations as list of movie titles in English
# recommendations = get_recommendations(user_of_interest, sim_mat, ratings_mat, num_of_recs, size_of_neighborhood)
# print(recommendations)

# movieDict = {}
# with open('movies.csv', encoding="utf8", errors='ignore') as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		movieDict[row[0]] = row[1]

# movieNameRecs = []
# for x in recommendations:
#     if str(x) in movieDict:
#         movieNameRecs.append(movieDict[str(x)])

# print(movieNameRecs)

ldadict = defaultdict(list)
for x in range(1,100):
	ldadict[str(x)] = get_recommendations(x, sim_mat, ratings_mat, num_of_recs, size_of_neighborhood)

f = open('rbm100.csv','r')
reader = csv.reader(f)
rbmdict = defaultdict(list)
for row in reader:
    rbmdict[row[1]].append(row[2])

#prints how many recommendations the methods had in common for each user
commonDict = {}
for key in ldadict.keys():
	commonDict[key] = len(set(ldadict[key])-(set(ldadict[key])-set(rbmdict[key])))
print(commonDict)

#divides by number of recommendations to get % similarity
for key in commonDict:    
    commonDict[key] /=  num_of_recs

#finds average similarity
_sum = 0
for key in commonDict:
    _sum += commonDict[key]
print((_sum/size_of_neighborhood) * 100)
