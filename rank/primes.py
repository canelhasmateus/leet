#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#


class Wheel:

	def __init__( self, basis ):
		self.basis = sorted( basis )
		self.len_cycle = 1
		for base in self.basis:
			self.len_cycle *= base

		coprime = lambda n: all( (n % base != 0 for base in basis) )
		cycles = (i for i in range( 2, self.len_cycle + 2 ))
		self.sequence = [ i for i in filter( coprime, cycles ) ]

	def candidates( self ):
		for i in self.basis:
			yield i

		loop = -1
		while True:
			loop += 1
			base = loop * self.len_cycle
			for element in self.sequence:
				current = base + element
				yield current


wheel = Wheel( [ 2, 3, 5, 7, 11 ] )


def primality( n ):
	bound = math.ceil( math.sqrt( n ) )
	candidates = wheel.candidates()
	if n < 2:
		return False
	while True:
		current = next( candidates )
		if current > bound:
			break
		if (n % current) == 0:
			return False

	return True


# Write your code here

if __name__ == '__main__':
	import time

	start = time.time()
	i = 0
	for n in range( 1_000_000_0 ):
		if primality( n ):
			i += 1

	print( i )
	finish = time.time()
	print( finish - start )
