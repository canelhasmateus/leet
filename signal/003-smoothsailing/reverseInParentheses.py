import time

def solution4(inputString):
	stack = []

	for x in inputString:
		if x == ")":
			tmp = ""
			while stack[-1] != "(":
				tmp += stack.pop()
			stack.pop() # pop the (
			for item in tmp:
				stack.append(item)
		else:
			stack.append(x)

	return "".join(stack)


def solution3(s):
	for i in range(len(s)):
		if s[i] == "(":
			start = i
		if s[i] == ")":
			end = i
			return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
	return s

def solution2(s):
	return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')

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
		def test2( self ):
			self.assertEquals( solution( "foo(bar)baz" ), "foorabbaz" )
		def test3( self ):
			self.assertEquals( solution( "foo(bar)baz(blim)" ), "foorabbazmilb" )
		def test4( self ):
			self.assertEquals( solution( "foo(bar(baz))blim" ), "foobazrabblim" )


	start= time.time()
	for i in range( 1000000 ):

		solution4( "foo(bar(baz))blim" )

	finish = time.time()

	print(finish - start)
	# unittest.main()
