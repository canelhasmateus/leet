from typing import Set


class Solution:
	def isPalindrome( self, param1 ):
		return solution( param1 )


def alpha( char ):
	return "a" <= char <= "z"


def num( char: str ):
	return "0" <= char <= "9"

def whitespace( char: str ):
	return char == " "


class PSet:

	def __init__( self, *predicates ):

		self.predicates = predicates

	def __contains__( self, item ):
		for pred in self.predicates:
			if pred( item ):
				return True

		return False


def solution( param1: str ):
	p, q = 0, len( param1 ) - 1
	param1 = param1.lower()
	allowed: Set[ str ] = PSet( alpha, num )
	while p < q:
		left = param1[ p ]
		right = param1[ q ]
		if left not in allowed:
			p += 1
			continue

		if right not in allowed:
			q -= 1
			continue

		p += 1
		q -= 1

		if left != right:
			return False

	return True


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "A man, a plan, a canal: Panama" ), True )

		def test2( self ):
			self.assertEquals( solution( "race a car" ), False )

		def test3( self ):
			self.assertEquals( solution( " " ), True )



	unittest.main()
