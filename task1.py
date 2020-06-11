#!/usr/bin/env python
import sys
import itertools 
import os   
from itertools import groupby
from operator import itemgetter 


# Function definitions

def pagination(pag, interv, my_dic, sorting_dic, mode, length_dic):
	
	print("\nUsing pagination function...")
    
    # Pagination
	if pag:
		if int(interv) > int(length_dic):
			print("There are only", length_dic, "elements")
		print("\nShowing", interv, "elements")
		count=0
		print("\nOrdering in descending mode...")
		for key, value in sorted(sorting_dic.items(), key = itemgetter(1), reverse = True):
			if count<=(int(ans4)-1):
				count +=1
				if mode=="3":
					print("Total request of", key, "is", value)
				elif mode=="4":
					print("Request percentage of", key, "is", value,"%")
				elif mode=="5":
					print("Total numbers of bits transfered of", key, "is", value, "bits")
			else:
				break
	# No pagination
	else:
		print("\nShowing all (", length_dic, ") elements")
		print("\nOrdering in descending mode...")
		for key, value in sorted(sorting_dic.items(), key = itemgetter(1), reverse = True):
			if mode=="3":
				print("Total request of", key, "is", value)
			elif mode=="4":
				print("Request percentage of", key, "is", value,"%")
			elif mode=="5":
				print("Total numbers of bits transfered of", key, "is", value, "bits")


def menu():
	
	print("""Welcome!""")
	
	ans1=input("What would you like to do?\n \
    	1.Group by IP\n \
    	2.Group by HTTP status code\n \
    	q.Exit/Quit\n \
    	--> ")
	if ans1=="1":
		print("\nGroup by IP")
	elif ans1=="2":
		print("\n Group by HTTP status code")
	elif ans1=="q":
		print("\n Goodbye!")
		sys.exit()
	else:
		print("\n Not Valid Choice")
		sys.exit()

	ans2=input("What do you want to do for each group?\n \
    	3.Request count\n \
    	4.Request count percentage of all logged requests\n \
    	5.Total number of bytes transferred\n \
    	--> ")
	if ans2=="3":
		print("\n Request count")
	elif ans2=="4":
		print("\n Request count percentage of all logged requests")
	elif ans2=="5":
		print("\n Total number of bytes transferred")
	elif ans2=="q":
		print("\n Goodbye!")
		sys.exit()
	else:
		print("\n Not Valid Choice")
		sys.exit()

	ans3=input("Do you want pagination?\n \
    	6.Enter pagination\n \
    	7.Showing all\n \
    	--> ")
	if ans3=="6":
		ans4=input("\n Enter pagination:")
	elif ans3=="7":
		print("\n Showing all")
		ans4=0
	elif ans3=="q":
		print("\n Goodbye!")
		sys.exit()
	else:
		print("\n Not Valid Choice")
		sys.exit() 
	
	return ans1, ans2, ans3, ans4


def grouping(mode, logfile): 
	
	my_list = []
	for line in logfile:
		x = line.split()
		my_list.append(x)
	# Remove empty lists from matrix
	my_list = [x for x in my_list if x != []]
	my_dic = dict()
	# Grouping by IP
	if mode=="1":
		f = lambda x: x[0]
	# Grouping by HTTP status code
	elif mode=="2":
		f = lambda x: x[8]
	for key, group in groupby(sorted(my_list, key=f), f):
	    my_dic[key] = list(group)
	
	return my_dic

def check_file(logfile):
		# Check if logfile is empty
		log = logfile.read(1)
		if not log:
			print("\n Log file is EMPTY!")
			sys.exit()	

'''
Example of using command line arguments
and reading a log file, line by line.
'''



if __name__ == '__main__':
	# Checking parameters
	if (len(sys.argv) != 2):
		print("Incorrect number of parameters, you have to specify log file\n")
		sys.exit()
	filename = sys.argv[1]
	with open(filename, 'r') as logfile:

		check_file(logfile)

		ans=True
		while ans:
			ans1, ans2, ans3, ans4 = menu()
			ans = False

		# Log file is not empty
		my_dic = grouping(ans1, logfile)

		# Request count
		if ans2=="3":
			print("Counting request...")
			# Create a dictionary to store key and value to descending sorter
			sorting_dic = {}
			length_dic = 0
			for key in my_dic:
			    length_key = len(my_dic[key])
			    length_dic += len(my_dic[key])			    
			    sorting_dic[key] = length_key
			for key in my_dic:
				length_key = len(my_dic[key])


		# Request count percentage of all logged requests
		if ans2=="4":
			print("Counting request percentage of all logged requests...")
			# Create a dictionary to store key and value to descending sorter
			sorting_dic = {}
			length_dic = 0
			for key in my_dic:
			    length_key = len(my_dic[key])			    
			    length_dic += len(my_dic[key])
			print("Total requests", length_dic)
			for key in my_dic:
				length_key = len(my_dic[key])
				sorting_dic[key] = (length_key/length_dic)*100


		# Total number of bytes transferred
		if ans2=="5":
			print("Calculating total number of bytes transferred...")
			# Create a dictionary to store key and value to descending sorter
			sorting_dic = {}
			length_dic = 0
			for key in my_dic:
				length_dic += len(my_dic[key])
				ind_log = my_dic.get(key,"")
				data_trans = 0
				for line in ind_log:
					# To ignore those log with - data transfered
					try:
						data_trans += int(line[9])
					except Exception:
					    pass
				sorting_dic[key] = data_trans
		
		# Pagination
		if ans3=="6":
			pagination(True, ans4, my_dic, sorting_dic, ans2, length_dic)
		if ans3=="7":
			pagination(False, 0, my_dic, sorting_dic, ans2, length_dic)

