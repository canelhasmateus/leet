
def solution( param1 ):


	size = len( param1)
	left = 0
	concat = ""
	while left < size:
		char = param1[left]

		if char == "(":
			depth = 1
			right = left + 1

			while depth > 0:
				rChar = param1[right]
				if rChar == ")":
					depth -= 1
				elif rChar == "(":
					depth += 1

				right += 1

			concat += solution( param1[ left + 1 : right - 1] )[::-1]
			left = right
		else:
			concat += char
			left += 1

	return concat


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "(bar)" ), "rab" )


	unittest.main()
