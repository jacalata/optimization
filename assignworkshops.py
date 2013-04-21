
import math


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
		print ("user day so far::", userSessions)
		print ("-current attendance at workshop", self.name, ":", self.sessions)
		for session in range(0,3):
			#print(user.name, pref, session)
			if self.sessions[session] < nSlots:
				if user.sessions[session] == 0:
					self.sessions[session] = self.sessions[session] + 1
					user.sessions[session] = self.idNumber
					print(user.name, "will attend workshop", self.name, "in session", session)
					return
				else:
					print (user.name, "is already busy in session", session)
			else:
				print("workshop", self.name, "slot", session, "is already full")

workshops = []

def initWorkshops():
	# can't use 0 based list because am using 0 for null workshop
	nullworkshop  = workshop()
	nullworkshop.name = "NULL"
	nullworkshop.sessions = [0,0,0]
	nullworkshop.idNumber = 0
	workshops.append(nullworkshop)

	workshopNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
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
				print (self.name, "is fully booked")
				return
			print ("pref: ", pref)
			if 0 in workshops[pref].sessions:		
				workshops[pref].findSpace(self.sessions)
			else:
				print ("workshop", pref, " has no free slots in any session")

	def showSchedule(self):
		print (workshops[self.sessions[0]].name, workshops[self.sessions[1]].name, workshops[self.sessions[2]].name)

users = []

def initUsers():

	# skip i/o
	tom = user("tom", [1,2,3,4,5,6,7,8,9,10])
	users.append(tom)

	sam = user("sam", [1,2,3,4,5,6,7,8,9,10])
	users.append(sam)

	n = len(users)
	for person in users:

	'''
	#region file reading
	read file
	n = 0
	for each line in file:
		newUser.name = name
		newUser.prefs = a, b, c, d, e, f
		#it would make this slightly easier if they had to rank all 10 options
		for option in options
			if option not in user.prefs
				newUser.prefs.append(option)
		n++
		users.append(newUser)
	'''

	return math.ceil(n/10.0)



#def __main__?
initWorkshops()

nSlots = initUsers()
print ("nslots", nSlots)
for user in users:
	print(user.name)
	print(user.prefs)
	user.assignByPreferences()
	user.showSchedule()
