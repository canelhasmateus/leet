import hypothesis.strategies as st
import pytest
from hypothesis import given, example, settings, Verbosity
from hypothesis.stateful import precondition


def solution( matrix ):
	haunted = set()
	res = 0

	for j in range( len( matrix[ 0 ] ) ):
		for i in range( len( matrix ) ):

			cost = matrix[ i ][ j ]

			if cost == 0:
				break

			res += cost

	return res


@settings( verbosity=Verbosity.verbose )
@given( st.integers(), st.integers() )
def test_1( a, b ):
	precondition( lambda : a > 10)
	if not a > 10:
		assert False

	assert True


@given( st.integers(), st.integers() )
def test_2( a, b ):
	matrix = [ [ 1, 1, 1, 0 ],
	           [ 0, 5, 0, 1 ],
	           [ 2, 1, 3, 10 ] ]

	assert solution( matrix ) == 9


if __name__ == '__main__':
	pytest.main( [ __file__, "-v" , "-s" ] )
