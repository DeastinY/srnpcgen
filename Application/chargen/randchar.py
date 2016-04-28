#!/usr/bin/python
# -*- coding: latin-1 -*-

import collections
import kivy
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
import random
import os

curdir = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(os.path.join(curdir, "randchar.kv"))

class Attribute():
	def __init__(self,name,prob):
		self.Name = name
		self.Prob = prob

	def __str__(self):
		return "{0}".format(self.Name)

	def __repr__(self):
		return self.__str__()

class RandChar(GridLayout):
	Gender = StringProperty()
	Metatype = StringProperty()
	Age = StringProperty()
	Traits = StringProperty()
	Special = StringProperty()
	Name = StringProperty()

	def __init__(self, **kwargs):
		super(RandChar, self).__init__(**kwargs)
		self.cols=1
		self.rows=7
		self.padding=10
		self.spacing=5
		self.RandAll()

	def __str__(self):
		return "{0}, {1}, {2} \n{3}".format(self.Gender, self.Metatype, self.Age, self.Traits)

	def RandAll(self):
		self.RandGender()
		self.RandMetatype()
		self.RandAge()
		self.RandTraits()
		self.RandSpecial()
		self.RandName()

	def RandGender(self):
		self.Gender=pick(gender)

	def RandMetatype(self):
		self.Metatype=pick(metatype)

	def RandAge(self):
		self.Age=pick(age)

	def RandTraits(self):
		traits = [pick(trait) for i in range(random.randint(1,5))]
		self.Traits=", ".join(traits)

	def RandSpecial(self):
		self.Special=pick(special)

	def RandName(self):
		name = ""
		if self.Gender=="Männlich":
			name = pick(names_male)
		elif self.Gender=="Weiblich":
			name = pick(names_female)
		else:
			name = "Error"
		street = pick(names_street)
		family = pick(names_family)
		self.Name= "{0} \"{1}\" {2} ".format(name,street,family)

def load(file):
	ret = []
	with open(os.path.join(curdir,file),"r") as f:
		lines = f.readlines()
		for l in lines:
			for r in ['\n','0','1','2','3','4','5','6','7','8','9','(',')']:
				l = l.replace(r,'')
			ret.append(Attribute(l.replace('\n',''), 1))
	return ret



def pick(atr):
	n = 0
	max = sum([a.Prob for a in atr])
	r = random.randint(0,max)
	for a in atr:
		n += a.Prob
		if n >= r:
			return a.Name

names_street = load('char_names_street.txt')
names_family = load('char_names_family.txt')
names_male = load('char_names_male.txt')
names_female = load('char_names_female.txt')
trait = load('char_traits.txt')
special = load('char_special.txt')
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
	Attribute('Erwachsen', 50),
	Attribute('Alt', 20)
	]
