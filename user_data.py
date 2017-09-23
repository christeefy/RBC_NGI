from random import randint
import json

def json_list(json_users):
	return json.dumps(json_users)


users = []

university_poss = ["UT", "RU", "UW"]
country_poss = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "USA"]
gender_poss = ["Male", "Female", "Prefer Not to Say"]
program_poss = ["Computer Science", "Finance", "HR", "Other"]

for i in xrange(0,31):
	user = {
		"identification": 0,
		"salary": 0,
		"university": "",
		"country": "",
		"gender": "",
		"age": 0,
		"years_worked": 0,
		"program": ""
	}

	#IDENTIFICATION (NAME)
	user["identification"] = i

	#SALARY
	user ["salary"] = randint(62,73)

	#UNIVERSITY
	user["university"] = university_poss[randint(0, 2)]

	#COUNTRY
	user["country"] = country_poss[randint(0,6)]

	#GENDER
	user["gender"] = gender_poss[randint(0,2)]

	#AGE
	user["age"] = randint(22,65)

	#NUMBER OF YEARS WORKED
	user["years_worked"] = randint (2,30)

	#UNIVERSITY PROGRAM
	user["program"] = program_poss[randint(0,3)]








	users.append(user)

# for x in xrange(0,31):
# 	print users[x]
# 	x = x+1

print json_list(users)




