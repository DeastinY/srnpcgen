#!/usr/bin/python
# -*- coding: latin-1 -*-

import collections
import kivy
import random
import os

class Attribute:
	def __init__(self,name,prob):
		self.Name = name
		self.Prob = prob

	def __str__(self):
		return "{0}".format(self.Name)

	def __repr__(self):
		return self.__str__()

class RandomCharacter:
	def __init__(self):
		self.Gender = pick(gender)
		self.Metatype = pick(metatype)
		self.Age = pick(age)
		self.Traits = []
		for i in range (random.randint(1,5)):
			self.Traits.append(pick(traits))

	def __str__(self):
		return "{0}, {1}, {2} \n{3}".format(self.Gender, self.Metatype, self.Age, self.Traits)

gender = [
	Attribute('Männlich', 50),
	Attribute('Weiblich', 50)
	]
metatype = [
	Attribute('Mensch', 45),
	Attribute('Natarki', 1),
	Attribute('Zwerg', 6),
	Attribute('Hanuman', 2),
	Attribute('Menehune', 2),
	Attribute('Gnom', 3),
	Attribute('Kokogroko', 2),
	Attribute('Ork', 5),
	Attribute('Hobgoblin', 3),
	Attribute('Oger', 2),
	Attribute('Oni', 2),
	Attribute('Satyr', 3),
	Attribute('Elf', 7),
	Attribute('Dryade', 3),
	Attribute('Wakyambi', 1),
	Attribute('Fotosynthese', 1),
	Attribute('Nächtliche', 3),
	Attribute('Troll', 5),
	Attribute('Riese',1),
	Attribute('Zyklop',1),
	Attribute('Minotaure',1),
	Attribute('Fomori',1)
	]

age = [
	Attribute('Jung', 30),
	Attribute('Normal', 50),
	Attribute('Alt', 20)
	]

traits = []
with open("char_traits.json","r+") as f:
	lines = f.readlines()
	for l in lines:
		traits.append(Attribute(l.replace('\n',''), 1))

def pick(atr):
	n = 0
	max = sum([a.Prob for a in atr])
	r = random.randint(0,max)
	for a in atr:
		n += a.Prob
		if n >= r:
			return a

print (RandomCharacter())
