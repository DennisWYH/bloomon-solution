import sys
from itertools import combinations 



class BloomonBouquetMaker:

	def __init__(self):
		# Create instance variables
		self.sFlowers = {}
		self.lFlowers = {}
		self.design_patterns = []
		self.design_implementations = []
		self.bouquets = []

	"""
	Argument: user stdin
	first lins contains design patterns of flower
	After empty line there is flower information 
	"""
	def processData(self,inputData):
		isDesign = True
		for i in inputData:
			if(isDesign):
				if(i == '\n'):
					isDesign = False
				else:
					# Before the empty space in the input, data should be designs
					self.design_patterns.append(i)
			else:
				# After emplty space in the input, data should be flowers
				self.countFlower(i)

	# This function read flower input data
	# Store the flower data in two dictionaries
	# sFlowers dictionary to store small flowers and their numbers
	# lFlowers dictionary to store large flowers and their numbers
	def countFlower(self,specie_and_size):
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



	def design_implementation(self,d):
		# For each design give, there are at least 1 implementations of the design.
		# This function returns all the posible implementations of a given design
		design_posibilities = [] 

		# Retrive the flower_species and maximal number requirement for each 
		chopped_d = d[2:-1]
		flower_species = [flower for flower in list(chopped_d) if flower.isalpha()]
		number_of_species = len(flower_species)
		max_flower_numbers = [int(number) for number in list(chopped_d) if not number.isalpha()]
		
		# Construct a flowers string represented only by flower alphabets
		total_quantity = int(d[-1])
		flowers_format_in_alphabet = [flower * number  for flower, number in zip(flower_species,max_flower_numbers)]
		flowers_format_in_string = ''.join(flowers_format_in_alphabet)
		flower_max_dic = {}
		for item in zip(flower_species,max_flower_numbers):
			flower_max_dic[item[0]]= item[1]
		
		design_posibilities = combinations(flowers_format_in_string, total_quantity)
		# filter out duplicate 
		design_posibilities = set(design_posibilities)
		# filter out combinations which doesn't contain whole set of flowers
		full_design = []
		for design in design_posibilities:
			containFullFlower = True
			for specie in flower_species:
				if(specie not in design):
					containFullFlower = False
			if(containFullFlower):
				full_design.append(design)
		# filter out combinations where flower number > max of that flower
		qualified_designs = []
		for design in design_posibilities:
			isTooMuch = False
			for flower in design:
				if(design.count(flower)>flower_max_dic[flower]):
					isTooMuch = True
			if(not isTooMuch):
				qualified_designs.append(design)
		# put back design name & flower size in front of each design
		for design in qualified_designs:
			temp = []
			for i in design:
				count = str(design.count(i))
				temp.append(count+i)
			temp = set(temp)
			design = d[:2]+ ''.join(temp)
			self.design_implementations.append(design)
		return self.design_implementations



	# argument0: [] a list of all posible designs, for exmaple ['AS1a2b', 'AS1b2a']
	# argument1: {} a dictionary of small Flowers
	# argument2: {} a dictionary of large flowers
	def make_bouquet(self):
		for design in self.design_implementations:
			enoughFlower = True
			while(enoughFlower):
				size = design[1]
				if(size=='S'):
					flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
					for flower_number in flower_number_couple:
						flower = flower_number[0]
						number = flower_number[1]
						# check if there is stil any flower of this specie in the storage
						if(flower not in self.sFlowers.keys()):
							enoughFlower = False
						else:
							# check if there storage is enough to make this bouquet.
							if(int(self.sFlowers[flower])<int(number)):
								enoughFlower = False
					if(enoughFlower):
						flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
						self.bouquets.append(design)
						print(design,file=sys.stdout)
						for flower_number in flower_number_couple:
							flower = flower_number[0]
							number = int(flower_number[1])
							if(self.sFlowers[flower]>number):
								self.sFlowers[flower] = self.sFlowers[flower]-number
							if(self.sFlowers[flower]==number):
								del self.sFlowers[flower]
				if(size=='L'):
					flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
					for flower_number in flower_number_couple:
						flower = flower_number[0]
						number = flower_number[1]
						# check if there is stil any flower of this specie in the storage
						if(flower not in self.lFlowers.keys()):
							enoughFlower = False
						else:
							# check if there storage is enough to make this bouquet.
							if(int(self.lFlowers[flower])<int(number)):
								enoughFlower = False
					if(enoughFlower):
						flower_number_couple = zip([flower for flower in design[3::2]],[number for number in design[2::2]])
						self.bouquets.append(design)
						print(design,file=sys.stdout)
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
	while(True):
		line = sys.stdin.readline()
		line = line.rstrip()
		print("raw input is line", line)
		if(isDesign):
			if(line==''):
				isDesign = False
				print("below is flower")
				print("all designs are ready.")
				print("designs are, " , bloomon.design_patterns)
				designs = bloomon.design_patterns
				for design in designs:
					bloomon.design_implementation(design)
			else:
				print("below is design")
				bloomon.design_patterns.append(line)
				print("current design patter is", bloomon.design_patterns)
		else:
			bloomon.countFlower(line)
			print("current flower is ",bloomon.sFlowers,bloomon.lFlowers)
			bloomon.make_bouquet()
