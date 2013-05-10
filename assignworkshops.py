
import math
import csv

VERBOSE = True
DEBUGLOG = False
users = []
workshops = []
#	workshopNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
nSlots = 0

class workshop:
	
	def __init__(self):
		sessions = [0,0,0]
		name = ""
		idNumber = 0

	def hasSpaceAvailable(self):
		for session in sessions:
			if session < nSlots:
				return true
		return false

	def findSpace(self, userSessions):		
		if (DEBUGLOG):
			print ("user day so far::", userSessions)
			print ("-current attendance at workshop", self.name, ":", self.sessions)
		for session in range(0,3):
			#print(user.name, pref, session)
			if self.sessions[session] < nSlots:
				if user.sessions[session] == 0:
					self.sessions[session] = self.sessions[session] + 1
					user.sessions[session] = self.idNumber
					if (VERBOSE):
						print(user.name, "will attend workshop", self.name, "in session", session)
					return
				else:
					if (VERBOSE):
						print (user.name, "is already busy in session", session)
			else:
				if (VERBOSE):
					print("workshop", self.name, "slot", session, "is already full")

def initWorkshops(workshopNames):
	# can't use 0 based list because am using 0 for null workshop
	if (DEBUGLOG):
		print("wshops:", workshopNames)
	nullworkshop  = workshop()
	nullworkshop.name = "NULL"
	nullworkshop.sessions = [0,0,0]
	nullworkshop.idNumber = 0
	workshops.append(nullworkshop)

	i = 1

	for name in workshopNames:
		current = workshop()
		current.name = name
		current.sessions = [0,0,0]
		current.idNumber = i
		workshops.append(current)
		i = i + 1

class user(object):

	def __init__(self, newname, newprefs):
		self.name = newname
		self.prefs = newprefs
		self.sessions = [0,0,0]	

	def assignByPreferences(self):
		# naive algorithm
		# if Tom and Sam are the two attendees, and both want to see (a,b,c,d)
		# this will result in tom seeing (a,b,c)
		# and sam seeing (b,a,d)
		for pref in self.prefs:
			if 0 not in self.sessions:
				if (VERBOSE):
					print (self.name, "is fully booked")
				return
			if 0 in workshops[pref].sessions:		
				workshops[pref].findSpace(self.sessions)
			else:
				if (VERBOSE):
					print ("workshop", pref, " has no free slots in any session")

	def showSchedule(self):
		print (workshops[self.sessions[0]].name, workshops[self.sessions[1]].name, workshops[self.sessions[2]].name)


def initialiseData():

	#region file reading
	reader = csv.reader(open('SampleData1.csv', newline=''), delimiter=',', quotechar='|')
	#line 1 = nWorkshops, workshopname1, workshopname2,...,workshopnameN
	#remaining lines = sam, preferenceID1, preferenceID2,...preferenceIDN
	n = 0
	for row in reader:
		if (DEBUGLOG):
			print (row)
		if (n == 0):
			nWorkshops = row[0]
			workshopNames = row[1:]
			initWorkshops(workshopNames)
		else:
			name = row[0]
			#prefs = map( int, row[1:])
			prefs = []
			for i in row[1:]:
				prefs.append(int(i))
			users.append(user(name, prefs))
		n = n+1

	n = len(users)
	return math.ceil(n/10.0)



#def __main__?

nSlots = initialiseData()
for user in users:
	print(user.name, ":", user.prefs)
	user.assignByPreferences()
	user.showSchedule()
