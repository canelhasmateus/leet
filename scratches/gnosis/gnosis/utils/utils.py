from typing import Mapping, Callable, TypeVar, Iterable

K = TypeVar( "K" )
V = TypeVar( "V" )


def map_with( func: Callable[ [ V ], K ], iterable: Iterable[ V ] ) -> Mapping[ K, V ]:
	return { func( value ): value for value in iterable }
