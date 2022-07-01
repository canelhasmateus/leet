from __future__ import annotations

from typing import TypeVar, Generic, Type, Optional, Callable

Boolean = bool
T = TypeVar( "T" )
U = TypeVar( "U" )


class Result( Generic[ T ] ):

	def __init__( self, value: T = None, exception: Exception = None ):

		self._value: Optional[ T ] = value
		self._exception: Optional[ Exception ] = exception

	def done_with( self, value: T ) -> None:
		self._value = value

	def fail_with( self, exception: Exception ) -> None:
		self._exception = exception

	def successful( self ) -> Boolean:
		return self._exception is not None and self._value is not None

	def map( self, func: Callable[ [ T ], U ] ) -> Result[ U ]:
		if self.successful():
			v = func( self.value() )
			return Result( v )
		else:
			return self

	def value( self ) -> T:
		if self._exception is not None:
			raise self._exception
		return self._value

	def __enter__( self ):
		return self

	def __exit__( self, exc_type: Type[ Exception ], exc_value: Exception, traceback ) -> Boolean:
		if exc_type is not None:
			self.fail_with( exc_value )

		return True
