import math


def solution( photo ):

	res = []

	for i in range( 1 , len( photo) - 1):
		row = photo[i]
		blurred_row = [ ]
		for j in range( 1 , len( row) - 1 ):


			above_below = sum( photo[ i - 1] ) + sum(photo[i  + 1])
			sides =row[ j - 1 ] +  row[ j + 1]
			element = row[j]
			blurred = (above_below + sides + element) / 9

			blurred_row.append( math.floor( blurred) )


		res.append( blurred_row)


	return res



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			image = [[1, 1, 1],
			         [1, 7, 1],
			         [1, 1, 1]]

			self.assertEquals( solution( image ) , [[ 1]] )


	unittest.main()
