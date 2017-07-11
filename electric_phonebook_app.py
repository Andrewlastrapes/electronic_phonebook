# dicton = True

# d = {}

# while dicton == True:
# 	print("\n")
# 	print("Electronic Phone Book")
# 	print("===================")
# 	entry = input("1. Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit \n \n What do you want to do(1-5)? ")
# 	if entry == "1":
# 		lookup = input("Who are you looking up?: ")
# 		if lookup in d:
# 			print("\n")
# 			print(d[lookup])
# 			print("\n")
# 		dicton = True	
# 	elif entry == "2":
# 		user_name_entry = input("Please enter the users name: ")
# 		user_number_entry = input("Please enter the users number: ")
# 		d[user_name_entry] = user_number_entry
# 		print("\n")
# 		print("Entry stored for " + user_name_entry)
# 		print("\n")
# 		dicton = True
# 	elif entry == "3":
# 		del_name = input("Whose information would you like to delete?: ")
# 		del d[del_name]
# 		print("\n")
# 		print("Your updated phonebook: \n" + str(d))
# 		print("\n")
# 		dicton = True
# 	elif entry == "4":
# 		print("\n")
# 		print(d)
# 		print("\n")
# 		dicton = True
# 	elif entry == "5":
# 		print("\n")
# 		print("Bye")
# 		print("\n")
# 		dicton = False


# make a function for each condition. 


def add_name(phonebook):
	new_name = input("Please enter new name: ")
	new_number = input("Please enter their number: ")
	phonebook[new_name] = new_number


def get_name():
	return input("Name: ")

	

def get_number():
	return input("Number: ")

def delete_entry(phonebook):
	delete1 = input("Whose information would you like to delete?: ")
	del phonebook[delete1]

def list_entries():
	print(d)







dicton = True

d = {}

while dicton == True:
	print("\n")
	print("Electronic Phone Book")
	print("===================")
	entry = input("1. Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit \n \n What do you want to do(1-5)? ")
	

	if entry == "1":
		

		dicton = True	
	
	elif entry == "2":
		add_name(d)
		dicton = True
	
	elif entry == "3":
		delete_entry(d)
		dicton = True

	elif entry == "4":
		list_entries()
		dicton = True
	
	elif entry == "5":
		print("\n")
		print("Bye")
		print("\n")
		dicton = False
















