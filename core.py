import random

class Actor:
	list = []
	deceased = []
	count = 0

	def __init__(self, name, district):
		self.name = name
		self.district = district
		self.alive = True
		self.female = False
		# these feel too... hacky
		# maybe in the future move the list somewhere else?
		Actor.list.append(self)
		Actor.count += 1

	def describe(self):
		print('Name:', self.name)
		print('Sex:', ['Male', 'Female'][self.female])
		print('District:', self.district)
		print('Status:', ['Dead', 'Alive'][self.alive])
	
	def describe_all():
		for actor in Actor.list + Actor.deceased:
			actor.describe()
			print()

	def nom(self):
		return ['he', 'she'][self.female]

	def acc(self):
		return ['him', 'her'][self.female]

	def die(self):
		Actor.count -= 1
		Actor.deceased.append(self)
		Actor.list.remove(self)

def assault(attacker, defender, debug = False):
	attack = random.randint(1,6)
	defend = random.randint(1,6)
	if debug:
		print("rolling {} for {}".format(attack, attacker.name))
		print("rolling {} for {}".format(defend, defender.name))

	if attack - defend > 1:
		print("{} brutally slays {}.".format(attacker.name, defender.name))
		defender.die()
	elif attack - defend < 2:
		print("{} assaults {}, but {} quickly overwhelms and kills {}.".format(attacker.name, defender.name, defender.nom(), attacker.acc()))
		attacker.die()
	else:
		print("{} attacks {}, but misses.".format(attacker.name, defender.name, defender.acc(), attacker.acc()))

def demo():
	Actor('Nix', 1)
	Actor('Kareem', 2)

demo()
