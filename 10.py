class Thing():
	pass
print(Thing())
example=Thing()
print(example)
class Thing2():
	letters='abc'
print(Thing2.letters)
class Thing3():
	def __init__(self):
		self.letters='xyz'
something=Thing3()
print(something.letters)
class Element():
	def __init__(self,name,symbol,number):
		self.__name=name
		self.__symbol=symbol
		self.__number=number
	@property
	def name(self):
		return self.__name
	@property
	def symbol(self):
		return self.__symbol
	@property
	def number(self):
		return self.__number
	
	def __str__(self):
		return ('name:=%s obozna4enie -%s nomer -%s' % (self.name,self.symbol,self.number))
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen=Element(**el_dict)
print(hydrogen)
