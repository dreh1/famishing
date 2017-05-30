import random

class Actor:
	list = []
	deceased = []
	count = 0

	def __init__(self, name, district, female = False):
		self.name = name
		self.district = district
		self.alive = True
		self.female = female
		self.strength = 0
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
		self.alive = False
		Actor.count -= 1
		Actor.deceased.append(self)
		Actor.list.remove(self)

def assault(attacker, defender, debug = False):
	attack = random.randint(1,6)
	defend = random.randint(1,6)
	if debug:
		print("rolling {}+{} for {}".format(attack, attacker.strength, attacker.name))
		print("rolling {}+{} for {}".format(defend, defender.strength, defender.name))
	attack += attacker.strength
	defend += defender.strength
	if debug:
		print("difference", attack - defend)

	if attack - defend > 1:
		print("{} brutally slays {}.".format(attacker.name, defender.name))
		defender.die()
	elif attack - defend < -1:
		print("{} assaults {}, but {} quickly overwhelms and kills {}.".format(attacker.name, defender.name, defender.nom(), attacker.acc()))
		attacker.die()
	else:
		print("{} attacks {}, but misses.".format(attacker.name, defender.name, defender.acc(), attacker.acc()))

def demo():
	Actor('Nix', 1)
	Actor('Kareem', 2)
	Actor.list[1].strength += 2
	Actor('Katka', 2, female = True)

demo()
