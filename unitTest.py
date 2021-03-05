from BloomonBouquetMaker import BloomonBouquetMaker
import unittest

class BloomonTestCase(unittest.TestCase):
    def setUp(self):
    	self.bloomon = BloomonBouquetMaker()

    def testCase1(self):
    	result = self.bloomon.design_implementation('AS2a2b3')
    	# result should be ['AS1a2b','AS2a1b']
    	self.assertEqual(len(result), 2)

    def testCase2(self):
    	result = self.bloomon.design_implementation('BL2a2')
    	# result should be ['BL2a']
    	self.assertEqual(len(result), 1)

    def testCase3(self):
    	result = self.bloomon.design_implementation('CL2a3b2c5')
    	# result should be ['CL1a2b2c','CL1a3b1c','CL2a1b2c','CL2a2b1c']
    	self.assertEqual(len(result), 4)

    def testCase4(self):
    	result = self.bloomon.design_implementation('AS2a2b3')
    	self.bloomon.sFlowers = {'a':2,'b':1}
    	# result should be ['AS2a1b']
    	self.bloomon.make_bouquet()
    	self.assertEqual(len(self.bloomon.bouquets), 1)

    def testCase5(self):
    	result = self.bloomon.design_implementation('BL2a2')
    	self.bloomon.sFlowers = {'a':2,'b':1}
    	self.bloomon.make_bouquet()
    	self.assertEqual(len(self.bloomon.bouquets), 0)

    def testCase6(self):
    	result = self.bloomon.design_implementation('BL2a2')
    	self.bloomon.sFlowers = {'a':2,'b':1}
    	self.bloomon.lFlowers = {'a':2,'b':1}
    	self.bloomon.make_bouquet()
    	self.assertEqual(len(self.bloomon.bouquets), 1)
    

if __name__ == "__main__":
	unittest.main()