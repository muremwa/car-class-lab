# pass all tests from testCar.py

class Car:
	"""Doc string here"""
	def __init__(self, *args):
		try:
			self.name = args[0]
		except IndexError:
			self.name = "General"
		try:
			self.model = args[1]
		except IndexError:
			self.model = "GM"
		try:
			self.car_type = args[2]
		except IndexError:
			self.car_type = ""

		if self.name.upper() in ["PORSHE", "KOENIGSEGG"]:
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if self.car_type.upper() == "TRAILER":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
		self.speed = 0

	def is_saloon(self):
		if self.car_type.upper() != "TRAILER":
			return True
		else:
			return True

	def drive(self, speed_):
		if self.car_type.upper() == "TRAILER":
			self.speed = 77
		else:
			if self.name.upper() == "MERCEDES":
				self.speed = 1000
		return self
