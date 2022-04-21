
def solution( param1 ):

	if param1 == "":
		return ""

	concat = [ "" for i in range( len(param1) )]


	leftProng = 0
	rightProng = len( param1 )

	while leftProng < rightProng:


		leftChar = param1[ leftProng ]
		rightChar = param1[ rightProng ]

		if leftChar == "(" or rightChar == ")":
			while rightChar != ")":
				rightProng -= 1
			while leftChar != "(":
				leftProng += 1

			parSolution = solution( param1[leftProng : rightProng] )
			concat[ leftProng:rightProng] = parSolution

		else:
			concat[leftProng] = leftChar
			concat[rightProng] = rightChar
			leftProng+=1
			rightProng-=1

	return "".join( concat )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "(bar)" ), "rab" )


	unittest.main()
