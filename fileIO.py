import csv


def initWorkshops():
	# can't use 0 based list because am using 0 for null workshop
	nullworkshop  = workshop()
	nullworkshop.name = "NULL"
	nullworkshop.sessions = [0,0,0]
	nullworkshop.idNumber = 0
	workshops.append(nullworkshop)

	#workshopNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
	i = 1

	for name in workshopNames:
		current = workshop()
		current.name = name
		current.sessions = [0,0,0]
		current.idNumber = i
		workshops.append(current)
		i = i + 1


reader = csv.reader(open('SampleData1.csv', newline=''), delimiter=',', quotechar='|')


#line 1 = nWorkshops, workshopname1, workshopname2,...,workshopnameN
#remaining lines = sam, preferenceID1, preferenceID2,...preferenceIDN
n = 0
for row in reader:
	if (n == 0):
		nWorkshops = row[0]
		workshopNames = row[1:]
		initWorkshops() #nWorkshops, workshops)
	else:
		newUser.name = row[0]
		newUser.prefs = row[1:]
		n = n+1
		users.append(newUser)


print ("nslots", nSlots)
for user in users:
	print(user.name)
	print(user.prefs)
	user.assignByPreferences()
	user.showSchedule()
