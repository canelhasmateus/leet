
from __future__ import annotations

import operator
from functools import reduce
from typing import Iterable, List


def my_format( value, length ):
	return bin( value ).replace( "0b", "" ).zfill( length )


def answer( nums: List[int], maximumBit: int):
	result = [ 0 for _ in nums]
	total_xor = 0
	extrema = 2 ** maximumBit - 1
	length = len(nums)
	print( extrema)

	for i in range( length):
		
		element = nums[i]
		total_xor = total_xor ^ element
		result[ length - i - 1 ] = extrema - total_xor

	return result


##
##

def test_a():
	assert answer( [ 0, 1, 1, 3 ], 2 ) == [ 0, 3, 2, 3 ]


def test_b():
	assert answer( [ 2, 3, 4, 7 ], 3 ) == [ 5, 2, 6, 5 ]


def test_c():
	assert answer( [ 0, 1, 2, 2, 5, 7 ], 3 ) == [ 4, 3, 6, 4, 6, 7 ]

