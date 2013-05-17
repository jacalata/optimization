
import math
import csv

SHOWRESULT = True
SHOWLOGIC = True
DEBUGLOG = False
debugfilename = "scheduledebug.log"
debugfile = open(debugfilename, 'w')
users = []
workshops = []

def output(*args):
	for arg in args:
		print(arg)
		debugfile.write(args.__str__())

#data object definitions
class workshop:
	
	def __init__(self):
		sessions = [0] * nSessions
		name = ""
		idNumber = 0

	def hasSpaceAvailable(self):
		for session in self.sessions:
			if session < nSlots:
				return True
		return False

	def clearSchedule(self):
		self.sessions = [0] * nSessions

def initWorkshops(workshopNames):
	# can't use 0 based list because am using 0 for null workshop
	if (DEBUGLOG):
		output("wshops:", workshopNames)
	nullworkshop  = workshop()
	nullworkshop.name = "NULL"
	nullworkshop.sessions = [0,0,0]
	nullworkshop.idNumber = 0
	workshops.append(nullworkshop)

	i = 1

	for name in workshopNames:
		current = workshop()
		current.name = name
		current.sessions = [0] * nSessions	
		current.idNumber = i
		workshops.append(current)
		i = i + 1

	if (DEBUGLOG):
		output("wshops:", workshopNames)

class user(object):

	def __init__(self, newname, newprefs):
		self.name = newname
		self.prefs = newprefs
		self.sessions = [0] * nSessions	

	def attend(self, session, workshop):
		self.sessions[session] = workshop.idNumber
		workshop.sessions[session] = workshop.sessions[session] + 1

	def cancel(self, session, workshop):
		self.sessions[session] = 0
		workshop.sessions[session] = workshop.sessions[session] - 1

	def assignByPreferences(self, algorithm):
		# naive algorithm
		# if Tom and Sam are the two attendees, and both want to see (a,b,c,d)
		# this will result in tom seeing (a,b,c)
		# and sam seeing (b,a,d)
		for pref in self.prefs:
			if 0 not in self.sessions:
				if (SHOWLOGIC):
					output (self.name, "is fully booked")
				return self.calculateScheduleQuality()
			if 0 in workshops[pref].sessions:		
				algorithm(workshops[pref], self.sessions)
			else:
				if (SHOWLOGIC):
					print ("workshop", pref, " has no free slots in any session")
		 
	def clearSchedule(self):
		self.sessions = [0] * nSessions	

	def showSchedule(self):
		if (SHOWRESULT):
			print (self.name, workshops[self.sessions[0]].name, workshops[self.sessions[1]].name, workshops[self.sessions[2]].name)

	def calculateScheduleQuality(self):
		score = 0; 
		for pref in self.prefs:
			if pref in self.sessions:
				score = score + pref
		for i in range(nSessions):
			score = score - i - 1 # difference between the preference they got and the top preferences they listed
			#ie if the highest preference they got was 5, then the score for that is 4
		return score

#data initialisation
def readInData():

	#region file reading
	reader = csv.reader(open('SampleData1.csv', newline=''), delimiter=',', quotechar='|')
	#line 1 = nWorkshops, workshopname1, workshopname2,...,workshopnameN
	#remaining lines = sam, preferenceID1, preferenceID2,...preferenceIDN
	n = 0
	for row in reader:
		if (DEBUGLOG):
			output (row)
		if (n == 0):
			nWorkshops = row[0]
			workshopNames = row[1:]
			if (DEBUGLOG):
				output("wshopsread:", workshopNames)
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
	return workshopNames, math.ceil(n/10.0)

def clearSchedules():
	for workshop in workshops:
		workshop.clearSchedule()
	for user in users:
		user.clearSchedule();


#algorithms to choose from
def naiveFindSpace(workshop, userSessions):		
	if (DEBUGLOG):
		output ("Naive algorithm")
		output ("user day so far::", userSessions)
		output ("-current attendance at workshop", workshop.name, ":", workshop.sessions)
	for session in range(0,3):
		#print(user.name, pref, session)
		if workshop.sessions[session] < nSlots:
			if user.sessions[session] == 0:
				user.attend(session, workshop)
				if (SHOWLOGIC):
					print(user.name, "will attend workshop", workshop.name, "in session", session)
				return
			else:
				if (SHOWLOGIC):
					print (user.name, "is already busy in session", session)
		else:
			if (SHOWLOGIC):
				print("workshop", workshop.name, "slot", session, "is already full")

def v2FindSpace(workshop, userSessions):
	if (DEBUGLOG):
		output ("Second algorithm")
		output ("user day so far::", userSessions)
		output ("-current attendance at workshop", workshop.name, ":", workshop.sessions)
	for session in range(0,nSessions):
		#print(user.name, pref, session)
		if workshop.sessions[session] < nSlots:
			if user.sessions[session] == 0:
				user.attend(session, workshop)
				if (SHOWLOGIC):
					print(user.name, "will attend workshop", workshop.name, "in session", session)
				return
	#there were no seats at our available times: pass through again and try rearranging our available times
	for session in range(0,nSessions):
		if workshop.sessions[session] < nSlots:
			# there is a seat in this workshop, but the user is attending another one at this time
			# get the id of what they are attending, and check if it has an open slot in one of the users
			# remaining open slots
			betterWorkshop = workshops[user.sessions[session]]
			if (betterWorkshop.hasSpaceAvailable() ):
				#check if there is an open seat in this workshop during one of the users remaining free sessions
				for freeSession in range(nSessions):
					if (DEBUGLOG):
						output(freeSession, user.sessions)
					if user.sessions[freeSession] == 0:
						if betterWorkshop.sessions[freeSession] == 0:
							user.cancel(session, betterWorkshop)
							user.attend(freeSession, betterWorkshop)
							user.attend(session, workshop)
							if (SHOWLOGIC):
								print(user.name, "has switched to attend workshop", workshop.name, "in session", session)
								print(user.name, "has switched to attend workshop", betterWorkshop.name, "in session", freeSession)
							return
		else:
			if (SHOWLOGIC):
				print("workshop", workshop.name, "slot", session, "is already full")

algorithms = [naiveFindSpace, v2FindSpace]

#def __main__?
nSessions = 3 # how many workshops you can attend in total
workshopNames, nSlots = readInData() #workshop names, n Seats per workshop
if (SHOWRESULT):
	print(workshopNames, nSlots)
scheduleQuality = [0] * len(algorithms) 

for i in range(len(algorithms)):
	if (SHOWRESULT):
		print("-------")
	scheduleQuality[i] = [] * len(users)
	for user in users:
		if (DEBUGLOG):
			output(user.name, ":", user.prefs)
			output(algorithms[i].__name__)
		score = user.assignByPreferences(algorithms[i])
		scheduleQuality[i].append(score)
		if (DEBUGLOG):
			output("score= ", score)
			output(scheduleQuality[i])
		user.showSchedule()
	#clear existing user schedule
	clearSchedules()

averages = [sum(x)/len(x) for x in scheduleQuality]
if (SHOWRESULT):
	print( [x.__name__ for x in algorithms])
	print("schedule scores are:", scheduleQuality)
	print("schedule averages are ", averages)

# graph schedule quality or something