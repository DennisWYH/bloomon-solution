import sys
from itertools import combinations 

"""Bloomon command line application

Authur: Yunhai Wang
Date: 05/03/2021
The command line applicaation is writen in Python3, to mimick a bouquet making process.
It contains a class BloomonBouquetMaker, as well as a main method.
"""

class BloomonBouquetMaker:
	"""A Class used to represent a BouquetMaker in Bloomon company.
	...

    Attributes
    ----------
    sFlowers : {}
        a dictionary to store small flowers {key: flower specie, value: flower number}
    lFlowers : str
        a dictionary to store large flowers {key: flower specie, value: flower number}
    design_patterns : []
        a list of designs given by user
    design_implementations : []
        a list of designs implementations generated from design patterns
	bouquets : []
		a list of bouquets that can be made out of the design & flowers

    Methods
    -------
    isValidDesign(d:str) -> bool
    	input validation method
    isValidFlower(f:str) -> bool
    	input validation method
    countFlower(specie_and_size: str) -> None
    	given a flowe_size string eg. 'aL'
    	store the flower to sFlowers or lFlowers dictionary
	design_implementation(d:str) -> [str]:
		given a deisng string. eg. 'AS2a2b3'
		return all posibile implementation of this design within design limitation
		eg. 'AS1a2b3' and 'AS2a1b3'
	def make_bouquet() -> [str]:
		this method will check sFlowrs, lFlowers, design_implementations and make bouquet if possible

	"""

	def __init__(self):
		self.sFlowers = {}
		self.lFlowers = {}
		self.design_patterns = []
		self.design_implementations = []
		self.bouquets = []

	def isValidDesign(self,d:str) -> bool:
		# Method yet to be refined.
		# Need to check if the Total quantity <= than sum of all the max value
		isValid = True
		return isValid


	def isValidFlower(self,f:str) -> bool:
		isValid = True
		if(len(f)!=2):
			isValid = False
		if(f[1]!='S' and f[1]!='L'):
			isValid = False
		if(not f[0].isalpha()):
			isValid = False
		return isValid

	def countFlower(self,specie_and_size: str) -> None:
		"""This function takes in a flowe_size string eg. 'aL'
	    	and store the flower to sFlowers or lFlowers dictionary
		"""

		specie = str(specie_and_size[0])
		size = str(specie_and_size[1])
		if(size=='L'):
			if specie in self.lFlowers.keys():
				updatedNumber = self.lFlowers[specie]+1
				self.lFlowers[specie] = int(updatedNumber)
			else:
				self.lFlowers[specie] = 1
		else:
			if specie in self.sFlowers.keys():
				updatedNumber = self.sFlowers[specie]+1
				self.sFlowers[specie] = int(updatedNumber)
			else:
				self.sFlowers[specie] = 1

	def design_implementation(self,d:str) -> [str]:
		"""For each design give, there are at least 1 implementations of the design.
		
		This function returns all the posible implementations of a given design
		Given a deisng string. eg. 'AS2a2b3'
		return all posibile implementation of this design within design limitation
		eg. 'AS1a2b3' and 'AS2a1b3'
		"""

		design_posibilities = [] 

		# Retrive the flower_species and maximal number requirement for each 
		chopped_d = d[2:-1]
		flower_species = [flower for flower in list(chopped_d) if flower.isalpha()]
		number_of_species = len(flower_species)
		max_flower_numbers = [int(number) for number in list(chopped_d) if not number.isalpha()]
		
		# Construct a flowers string represented only by flower alphabets 'aabbb'
		total_quantity = int(d[-1])
		flowers_format_in_alphabet = [flower * number  for flower, number in zip(flower_species,max_flower_numbers)]
		flowers_format_in_string = ''.join(flowers_format_in_alphabet)
		flower_max_dic = {}
		for item in zip(flower_species,max_flower_numbers):
			flower_max_dic[item[0]]= item[1]
		
		design_posibilities = combinations(flowers_format_in_string, total_quantity)
		# filter out duplicate designs
		design_posibilities = set(design_posibilities)
		# filter out combinations which doesn't contain whole set of flowers, eg. lack flower a or b
		full_design = []
		for design in design_posibilities:
			containFullFlower = True
			for specie in flower_species:
				if(specie not in design):
					containFullFlower = False
			if(containFullFlower):
				full_design.append(design)
		# filter out combinations where flower number > max of that flower in the design
		qualified_designs = []
		for design in full_design:
			isTooMuch = False
			for flower in design:
				if(design.count(flower)>flower_max_dic[flower]):
					isTooMuch = True
			if(not isTooMuch):
				qualified_designs.append(design)
		# put back design name & flower size in front of each design, to form a letal design name
		for design in qualified_designs:
			temp = []
			for i in design:
				count = str(design.count(i))
				temp.append(count+i)
			temp = set(temp)
			design = d[:2]+ ''.join(temp)
			self.design_implementations.append(design)
		return self.design_implementations


	def make_bouquet(self) -> [str]:
		"""this method will check sFlowrs, lFlowers, design_implementations and make bouquets if possible
		Return type bouquets []
		it also output stdout of bouquets whenever possible
		"""
		
		for design in self.design_implementations:
			# Check all the designs that are possible against both sFlowers and lFlowers dictionary.
			enoughFlower = True
			while(enoughFlower):
				size = design[1]
				if(size=='S'):
					# If the design requires S flowers, check if sFLowers dictionary has enough flower to make this design
					flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
					for flower_number in flower_number_couple:
						flower = flower_number[0]
						number = flower_number[1]
						if(self.sFlowers.keys is not None):
							# check if there is stil any flower of this specie in the storage
							if(flower not in self.sFlowers.keys()):
								enoughFlower = False
							else:
								# check if there storage is enough to make this bouquet.
								if(int(self.sFlowers[flower])<int(number)):
									enoughFlower = False
						else:
							enoughFlower = Flase
					# If there is enough flower to make bouquet, make a bouquet and update the flower dictionary
					if(enoughFlower):
						flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
						# add this bouquet to the result, stdout the result 
						self.bouquets.append(design)
						print(design,file=sys.stdout)
						# update the flower storage in the dictionary
						for flower_number in flower_number_couple:
							flower = flower_number[0]
							number = int(flower_number[1])
							if(self.sFlowers[flower]>number):
								self.sFlowers[flower] = self.sFlowers[flower]-number
							if(self.sFlowers[flower]==number):
								del self.sFlowers[flower]
				if(size=='L'):
					# If the design requires L flowers, check if lFLowers dictionary has enough flower to make this design
					flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
					for flower_number in flower_number_couple:
						flower = flower_number[0]
						number = flower_number[1]
						if(self.lFlowers.keys is not None):
							# check if there is stil any flower of this specie in the storage
							if(flower not in self.lFlowers.keys()):
								enoughFlower = False
							else:
								# check if there storage is enough to make this bouquet.
								if(int(self.lFlowers[flower])<int(number)):
									enoughFlower = False
						else:
							enoughFlower = False
					# If there is enough flower to make bouquet, make a bouquet and update the flower dictionary
					if(enoughFlower):
						flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
						# add this bouquet to the result, stdout the result 
						self.bouquets.append(design)
						print(design,file=sys.stdout)
						# update the flower storage in the dictionary
						for flower_number in flower_number_couple:
							flower = flower_number[0]
							number = int(flower_number[1])
							if(self.lFlowers[flower]>number):
								self.lFlowers[flower] = self.lFlowers[flower]-number
							if(self.lFlowers[flower]==number):
								del self.lFlowers[flower]
		return self.bouquets

if __name__ == "__main__":
	bloomon = BloomonBouquetMaker()
	isDesign = True
	# keep taking input from user stdin
	while(True):
		try:
			line = str(sys.stdin.readline())
			line = line.rstrip()
		except ValueError:
			print("Oops, the value type is not as expected.")
		# If user input is flower design
		if(isDesign):
			if(line==''):
				isDesign = False
				designs = bloomon.design_patterns
				for design in designs:
					bloomon.design_implementation(design)
			else:
				if(bloomon.isValidDesign(line)):
					bloomon.design_patterns.append(line)
				else:
					print("Invalid Design. Please restart the application and try again.", file=sys.stdout)

		# If user input is flower info
		else:
			# Value validation
			if(bloomon.isValidFlower(line)):
				bloomon.countFlower(line)
				bloomon.make_bouquet()
			else:
				print("Invalid Flower. Please restart the application and try again.", file=sys.stdout)
