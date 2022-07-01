from __future__ import annotations

import functools
import heapq
from dataclasses import dataclass
from typing import Iterable


@functools.total_ordering
@dataclass
class ListNode:
	value: int
	next: ListNode | None

	@classmethod
	def of( cls, it: Iterable[ int ] ) -> ListNode:
		match it:
			case [ head, *tail ]:
				return ListNode( head, next = ListNode.of( tail ) )
			case _:
				return None

	def __le__( self, other ):
		return self.value <= other.value


class Solution:
	def mergeTwoLists( self, param1, param2 ):
		return solution( param1, param2 )


def myupdate( head, minimum ):
	if not head:
		return minimum
	if not minimum:
		return head

	head.next = minimum
	return head.next


def solution( param1, param2 ):
	leftHead = param1
	rightHead = param2
	root = ListNode( None, None)
	current = root
	while leftHead and rightHead:
		if leftHead <= rightHead:
			current.next = leftHead
			leftHead = leftHead.next
		else:
			current.next = rightHead
			rightHead = rightHead.next

		current = current.next

	if rightHead:
		current.next = rightHead
	elif leftHead:
		current.next = leftHead

	return root.next


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( ListNode.of( [ 1, 2, 4 ] ),
			                             ListNode.of( [ 1, 3, 4 ] ) ),
			                   ListNode.of( [ 1, 1, 2, 3, 4, 4 ] ) )


	unittest.main()
