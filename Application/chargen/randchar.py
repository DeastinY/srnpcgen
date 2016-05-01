#!/usr/bin/python
# -*- coding: latin-1 -*-

import collections
import json
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
		if self.Gender==u"Männlich":
			name = pick(names_male)
		elif self.Gender==u"Weiblich":
			name = pick(names_female)
		else:
			name = "Error"
		street = pick(names_street)
		family = pick(names_family)
		self.Name= u"{0} \"{1}\" {2} ".format(name,street,family)

	def ToJSON(self):
		j = {
			"Name" : self.Name,
			"Gender" : self.Gender,
			"Metatype" : self.Metatype,
			"Age" : self.Age,
			"Traits" : self.Traits,
			"Special" : self.Special
		}
		return json.dumps(j, indent=4)

	@staticmethod
	def FromJSON(j):
		r = RandChar()
		r.Name = j["Name"]
		r.Gender = j["Gender"]
		r.Metatype = j["Metatype"]
		r.Age = j["Age"]
		r.Traits = j["Traits"]
		r.Special = j["Special"]
		return r

def load(file):
	ret = []
	with open(os.path.join(curdir,file),"r") as f:
		lines = f.readlines()
		for l in lines:
			for r in ['\n','0','1','2','3','4','5','6','7','8','9','(',')']:
				l = l.replace(r,'')
			l = l.decode("utf-8","replace")
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
	Attribute(u'Männlich', 50),
	Attribute(u'Weiblich', 50)
	]
metatype = [
	Attribute(u'Mensch', 45),
	Attribute(u'Natarki', 1),
	Attribute(u'Zwerg', 6),
	Attribute(u'Hanuman', 2),
	Attribute(u'Menehune', 2),
	Attribute(u'Gnom', 3),
	Attribute(u'Kokogroko', 2),
	Attribute(u'Ork', 5),
	Attribute(u'Hobgoblin', 3),
	Attribute(u'Oger', 2),
	Attribute(u'Oni', 2),
	Attribute(u'Satyr', 3),
	Attribute(u'Elf', 7),
	Attribute(u'Dryade', 3),
	Attribute(u'Wakyambi', 1),
	Attribute(u'Fotosynthese', 1),
	Attribute(u'Nächtliche', 3),
	Attribute(u'Troll', 5),
	Attribute(u'Riese',1),
	Attribute(u'Zyklop',1),
	Attribute(u'Minotaure',1),
	Attribute(u'Fomori',1)
	]
age = [
	Attribute(u'Jung', 30),
	Attribute(u'Erwachsen', 50),
	Attribute(u'Alt', 20)
	]
