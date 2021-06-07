class Bear():
	def eats(self):
		return 'berries'
class Rabbit():
	def eats(self):
		return 'clover'
class Octotorpe():
	def eats(self):
		return 'campers'
mishka=Bear()
print(mishka.eats())
class Robot:
	def __init__(self):
		self.laser=Bear()
		self.claw=Rabbit()
		self.smartphone=Octotorpe()
	def does(self):
		return ''' I have many attachments :
My laser, to %s.
My claw to %s.
my smartphone to %s ''' % ( self.laser.eats() , self.claw.eats(), self.smartphone.eats())
robbie=Robot()
print(robbie.does())